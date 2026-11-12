
import os
import sqlite3
import uuid

from flask import (
    Flask, render_template, request, redirect, url_for,
    session, flash, send_from_directory, jsonify
)

import disease_advice

from disease_advice import (
    get_disease_advice,
    calculate_spray_quantity,
    normalize_disease
)

from predict_updated import (
    predict_disease,
    validate_tomato,
    get_disease_info
)

from severity_analysis import analyze_leaf_severity

# ============================================================
# APP CONFIGURATION
# ============================================================

app = Flask(__name__)
app.secret_key = os.environ.get(
    "LEAFVISION_SECRET_KEY",
    "change-this-secret-key-before-deployment"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
DATABASE = os.path.join(BASE_DIR, "leafvision.db")

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 40 * 1024 * 1024

# ============================================================
# TRANSLATIONS - ENGLISH AND MARATHI
# ============================================================

try:
    from translations import (
        TRANSLATIONS,
        get_translation,
        SUPPORTED_LANGUAGES as _LANGUAGES
    )
except ImportError:
    TRANSLATIONS = {}
    _LANGUAGES = {
        "en": "English",
        "mr": "मराठी"
    }

    def get_translation(key, language="en"):
        value = TRANSLATIONS.get(key, key)
        if isinstance(value, dict):
            return value.get(language, value.get("en", key))
        return value


if isinstance(_LANGUAGES, dict):
    SUPPORTED_LANGUAGES = {
        key: value for key, value in _LANGUAGES.items()
        if key in ("en", "mr")
    }
else:
    SUPPORTED_LANGUAGES = {
        key: key for key in _LANGUAGES
        if key in ("en", "mr")
    }

if not SUPPORTED_LANGUAGES:
    SUPPORTED_LANGUAGES = {
        "en": "English",
        "mr": "मराठी"
    }

for translation_value in TRANSLATIONS.values():
    if isinstance(translation_value, dict):
        translation_value.pop("hi", None)

FALLBACK_TRANSLATIONS = {
    "unsupported_plant": {
        "en": "Unsupported Plant",
        "mr": "असमर्थित वनस्पती"
    },
    "not_tomato": {
        "en": (
            "This image does not appear to be a tomato plant. "
            "Please upload a clear tomato leaf or plant image."
        ),
        "mr": (
            "ही प्रतिमा टोमॅटोच्या रोपाची दिसत नाही. "
            "कृपया टोमॅटोच्या पानाची किंवा रोपाची स्पष्ट प्रतिमा अपलोड करा."
        )
    },
    "upload_tomato": {
        "en": "Please Upload a Tomato Plant Image",
        "mr": "कृपया टोमॅटोच्या रोपाची प्रतिमा अपलोड करा"
    },
    "try_another": {
        "en": "Try Another Image",
        "mr": "दुसरी प्रतिमा वापरा"
    }
}

# ============================================================
# AI IMPORTS
# ============================================================

try:
    from predict_updated import (
        predict_disease,
        validate_tomato,
        get_disease_info
    )
except Exception as exc:
    print("WARNING: AI module could not be imported:", repr(exc))
    predict_disease = None
    validate_tomato = None
    get_disease_info = None

# ============================================================
# BUILT-IN ACCOUNTS
# ============================================================

BUILT_IN_USERS = {
    "admin@leafvision.ai": {
        "name": "LeafVision Admin",
        "password": "admin123",
        "role": "admin"
    },
    "farmer@leafvision.ai": {
        "name": "Farmer Expert",
        "password": "farmer123",
        "role": "farmer"
    }
}

# ============================================================
# DATABASE
# ============================================================

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def add_column_if_missing(cursor, table, column, definition):
    columns = cursor.execute(
        f"PRAGMA table_info({table})"
    ).fetchall()

    existing_columns = [item[1] for item in columns]

    if column not in existing_columns:
        cursor.execute(
            f"ALTER TABLE {table} ADD COLUMN {column} {definition}"
        )


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            image_filename TEXT,
            plant_part TEXT,
            symptoms TEXT,
            duration TEXT,
            growth_stage TEXT,
            environment TEXT,
            disease TEXT,
            confidence REAL,
            plant_verified REAL,
            tomato_status TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    for column, definition in [
        ("leaf_image_filename", "TEXT"),
        ("stem_image_filename", "TEXT"),
        ("root_image_filename", "TEXT"),
        ("whole_plant_image_filename", "TEXT")
    ]:
        add_column_if_missing(
            cursor, "analyses", column, definition
        )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS farmer_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            analysis_id INTEGER NOT NULL,
            farmer_id INTEGER NOT NULL,
            farmer_name TEXT NOT NULL,
            response TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(analysis_id) REFERENCES analyses(id),
            FOREIGN KEY(farmer_id) REFERENCES users(id)
        )
    """)

    for email, account in BUILT_IN_USERS.items():
        existing = cursor.execute(
            "SELECT id FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        if not existing:
            cursor.execute("""
                INSERT INTO users (name, email, password, role)
                VALUES (?, ?, ?, ?)
            """, (
                account["name"],
                email,
                account["password"],
                account["role"]
            ))

    conn.commit()
    conn.close()


init_db()

# ============================================================
# TEMPLATE GLOBALS AND LANGUAGE
# ============================================================

@app.context_processor
def inject_globals():
    language = session.get("language", "en")

    if language not in ("en", "mr"):
        language = "en"

    def t(key):
        translated = get_translation(key, language)

        if (
            translated == key
            and key in FALLBACK_TRANSLATIONS
        ):
            return FALLBACK_TRANSLATIONS[key].get(
                language,
                FALLBACK_TRANSLATIONS[key]["en"]
            )

        return translated

    return {
        "t": t,
        "current_language": language,
        "current_user": session.get("user"),
        "current_role": session.get("role"),
        "supported_languages": SUPPORTED_LANGUAGES
    }


@app.route("/language/<language>")
def change_language(language):
    session["language"] = (
        language if language in ("en", "mr") else "en"
    )
    return redirect(request.referrer or url_for("index"))


# ============================================================
# GENERAL HELPERS
# ============================================================

def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


def save_uploaded_image(file):
    if not file or not file.filename:
        return None

    if not allowed_file(file.filename):
        return None

    extension = file.filename.rsplit(".", 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{extension}"
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)
    return filename


def login_required():
    return "user_id" in session


def role_required(role):
    return (
        login_required()
        and session.get("role") == role
    )


def error_page(message, status=400):
    return render_template(
        "error.html",
        message=message
    ), status


# ============================================================
# DISEASE ADVICE - ENGLISH AND MARATHI
# ============================================================

def get_advice(disease, growth_stage=None):

    language = session.get("language", "en")

    if language not in ("en", "mr"):
        language = "en"

    print("\n========== LEAFVISION DISEASE ADVICE ==========")
    print("Advice module location:", disease_advice.__file__)
    print("Original AI disease label:", repr(disease))

    # Convert the AI model label into the database disease key.
    disease_key = normalize_disease(disease)

    print("Normalized disease key:", repr(disease_key))

    if disease_key is None:
        raise ValueError(
            f"Disease label not found in disease_advice.py: {disease}"
        )

    # Fetch the actual disease-specific data.
    advice = get_disease_advice(
        disease_name=disease_key,
        language=language,
        growth_stage=growth_stage
    )

    if not isinstance(advice, dict):
        raise TypeError("get_disease_advice() did not return a dictionary")

    # Preserve all original disease advice fields.
    advice = dict(advice)

    # Make sure result.html receives the correct fields.
    advice["treatment"] = advice.get("application", [])
    advice["application"] = advice.get("application", [])
    advice["prevention"] = advice.get("prevention", [])
    advice["precautions"] = advice.get("precautions", [])

    print("Matched disease:", advice.get("name"))
    print("Cause:", advice.get("cause"))
    print("Treatment:", advice.get("application"))
    print("Prevention:", advice.get("prevention"))
    print("Precautions:", advice.get("precautions"))
    print("Fertilizer:", advice.get("fertilizer"))
    print("Source:", advice.get("source"))
    print("================================================\n")

    return advice

# ============================================================
# LEAF DAMAGE / SEVERITY ANALYSIS
# ============================================================

def get_severity_result(image_filename):

    empty_result = {
        "affected_percentage": None,
        "remaining_percentage": None,
        "severity_stage": None,
        "severity_advice": None,
        "severity_overlay": None
    }

    if not image_filename:
        return empty_result

    image_path = os.path.join(
        UPLOAD_FOLDER,
        image_filename
    )

    if not os.path.isfile(image_path):
        print("Severity analysis skipped: image file not found.")
        return empty_result

    try:
        result = analyze_leaf_severity(image_path) or {}

        return {
            "affected_percentage": result.get("affected_percentage"),
            "remaining_percentage": result.get("remaining_percentage"),
            "severity_stage": result.get("severity_stage"),
            "severity_advice": result.get("severity_advice"),
            "severity_overlay": result.get("severity_overlay")
        }

    except Exception as exc:
        print("Severity analysis error:", repr(exc))
        return empty_result


# ============================================================
# HOME AND IMAGE ROUTES
# ============================================================

@app.route("/")
def index():
    return render_template("index_updated.html")


@app.route("/analyze", methods=["GET"])
@app.route("/analyze/", methods=["GET"])
def analyze():
    if not login_required():
        flash(
            "Please login first to analyze a new plant.",
            "error"
        )
        return redirect(url_for("login"))

    return render_template("analyze.html")


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@app.route("/uploads/analysis/<int:analysis_id>/<path:filename>")
def uploaded_analysis_file(analysis_id, filename):
    if not login_required():
        return redirect(url_for("login"))

    conn = get_db()

    analysis = conn.execute("""
        SELECT user_id, leaf_image_filename,
               stem_image_filename, root_image_filename,
               whole_plant_image_filename
        FROM analyses
        WHERE id = ?
    """, (analysis_id,)).fetchone()

    conn.close()

    if not analysis:
        return error_page("Analysis not found.", 404)

    if (
        session.get("role") == "user"
        and analysis["user_id"] != session.get("user_id")
    ):
        return error_page(
            "You are not allowed to view this image.",
            403
        )

    allowed_names = {
        analysis["leaf_image_filename"],
        analysis["stem_image_filename"],
        analysis["root_image_filename"],
        analysis["whole_plant_image_filename"]
    }

    if filename not in allowed_names:
        return error_page("Image not found.", 404)

    return send_from_directory(UPLOAD_FOLDER, filename)


# ============================================================
# SIGNUP
# ============================================================

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("Please fill all fields.", "error")
            return redirect(url_for("signup"))

        if email in BUILT_IN_USERS:
            flash("This email is reserved.", "error")
            return redirect(url_for("signup"))

        conn = get_db()

        try:
            conn.execute("""
                INSERT INTO users (name, email, password, role)
                VALUES (?, ?, ?, 'user')
            """, (name, email, password))

            conn.commit()

        except sqlite3.IntegrityError:
            flash("Email already registered.", "error")
            return redirect(url_for("signup"))

        finally:
            conn.close()

        flash(
            "Account created successfully. Please login.",
            "success"
        )
        return redirect(url_for("login"))

    return render_template("signup.html")


# ============================================================
# LOGIN AND LOGOUT
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        conn = get_db()

        user = conn.execute("""
            SELECT *
            FROM users
            WHERE email = ? AND password = ?
        """, (email, password)).fetchone()

        conn.close()

        if user:
            session.clear()

            session["user_id"] = user["id"]
            session["user"] = {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"]
            }
            session["role"] = user["role"]

            if user["role"] == "admin":
                return redirect(url_for("admin_dashboard"))

            if user["role"] == "farmer":
                return redirect(url_for("farmer_dashboard"))

            return redirect(url_for("index"))

        flash("Invalid email or password.", "error")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# ============================================================
# PLANT PREDICTION
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    if not login_required():
        return redirect(url_for("login"))

    leaf_file = request.files.get("leaf_image")
    stem_file = request.files.get("stem_image")
    root_file = request.files.get("root_image")
    whole_file = request.files.get("whole_plant_image")

    if not leaf_file or not leaf_file.filename:
        flash("Leaf image is required.", "error")
        return redirect(url_for("index"))

    leaf_filename = save_uploaded_image(leaf_file)

    if not leaf_filename:
        flash(
            "Invalid leaf image. Use JPG, JPEG, PNG, or WEBP.",
            "error"
        )
        return redirect(url_for("index"))

    stem_filename = save_uploaded_image(stem_file)
    root_filename = save_uploaded_image(root_file)
    whole_filename = save_uploaded_image(whole_file)

    plant_part = request.form.get("plant_part", "All")
    symptoms = request.form.get("symptoms", "").strip()
    duration = request.form.get("duration", "").strip()
    growth_stage = request.form.get("growth_stage", "").strip()
    environment = request.form.get("environment", "").strip()

    leaf_path = os.path.join(
        UPLOAD_FOLDER,
        leaf_filename
    )

    if validate_tomato is None or predict_disease is None:
        return error_page(
            "AI validation is unavailable. Check predict_updated.py "
            "and the model files.",
            503
        )

    try:
        # Step 1: Validate tomato image.
        validation = validate_tomato(leaf_path)
        print("Tomato validator result:", validation)

        tomato_confidence = float(
            validation.get("tomato_confidence", 0.0)
        )

        other_confidence = float(
            validation.get("other_confidence", 0.0)
        )

        if not validation.get("is_tomato", False):
            return render_template(
                "unsupported.html",
                leaf_image=leaf_filename,
                tomato_confidence=tomato_confidence,
                other_confidence=other_confidence
            )

        # Step 2: Predict disease.
        result = predict_disease(leaf_path)
        print("Final AI result:", result)

        if not result.get("is_tomato", False):
            return render_template(
                "unsupported.html",
                leaf_image=leaf_filename,
                tomato_confidence=float(
                    result.get(
                        "tomato_confidence",
                        tomato_confidence
                    )
                ),
                other_confidence=float(
                    result.get(
                        "other_confidence",
                        other_confidence
                    )
                )
            )

    except Exception as exc:
        print("AI prediction error:", repr(exc))

        return error_page(
            "Unable to analyze this image. Please upload a clear "
            "tomato plant image and try again.",
            500
        )

    plant_verified = tomato_confidence

    disease = (
        result.get("disease")
        or result.get("label")
        or "Unknown"
    )

    confidence = float(
        result.get("confidence", 0.0)
    )

    tomato_status = "Tomato Plant"

    disease_info = {}

    if get_disease_info:
        disease_info = get_disease_info(
            result.get("label", disease)
        ) or {}

    # Save analysis in database.
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO analyses (
            user_id,
            image_filename,
            leaf_image_filename,
            stem_image_filename,
            root_image_filename,
            whole_plant_image_filename,
            plant_part,
            symptoms,
            duration,
            growth_stage,
            environment,
            disease,
            confidence,
            plant_verified,
            tomato_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user_id"],
        leaf_filename,
        leaf_filename,
        stem_filename,
        root_filename,
        whole_filename,
        plant_part,
        symptoms,
        duration,
        growth_stage,
        environment,
        disease,
        confidence,
        plant_verified,
        tomato_status
    ))

    analysis_id = cursor.lastrowid

    conn.commit()
    conn.close()

    # Get disease-specific advice in selected language.
    advice = get_advice(disease, growth_stage)

    # Calculate approximate leaf damage.
    severity_result = get_severity_result(leaf_filename)

    return render_template(
        "result.html",
        analysis_id=analysis_id,
        image_filename=leaf_filename,
        leaf_image_filename=leaf_filename,
        stem_image_filename=stem_filename,
        root_image_filename=root_filename,
        whole_plant_image_filename=whole_filename,
        plant_part=plant_part,
        disease=disease,
        confidence=confidence,
        plant_verified=plant_verified,
        tomato_status=tomato_status,
        disease_info=disease_info,
        prediction=result,

        # Complete disease advice object.
        # Complete disease advice object.
advice=advice,

# Disease-specific treatment and prevention.
treatment=advice.get("application", []),
prevention=advice.get("prevention", []),
application=advice.get("application", []),
precautions=advice.get("precautions", []),

        symptoms=symptoms,
        duration=duration,
        growth_stage=growth_stage,
        environment=environment,
        farmer_responses=[],

        # Severity analysis.
        affected_percentage=severity_result["affected_percentage"],
        remaining_percentage=severity_result["remaining_percentage"],
        severity_stage=severity_result["severity_stage"],
        severity_advice=severity_result["severity_advice"],
        severity_overlay=severity_result["severity_overlay"]
    )


# ============================================================
# ACRE + 15 LITRE SPRAY CALCULATOR API
# ============================================================

@app.route("/api/spray-calculation", methods=["POST"])
def spray_calculation_api():

    if not login_required():
        return jsonify({
            "success": False,
            "error": "Please login first."
        }), 401

    data = request.get_json(silent=True) or request.form

    disease_name = data.get("disease", "").strip()

    try:
        area_acres = float(
            data.get("area_acres", 0)
        )

        calculation = calculate_spray_quantity(
            disease_name=disease_name,
            area_acres=area_acres,
            tank_capacity=15,
            language=session.get("language", "en")
        )

        return jsonify({
            "success": True,
            "calculation": calculation
        })

    except (ValueError, TypeError) as exc:
        return jsonify({
            "success": False,
            "error": str(exc)
        }), 400

    except Exception as exc:
        print("Spray calculation error:", repr(exc))

        return jsonify({
            "success": False,
            "error": "Unable to calculate the spray quantity."
        }), 500


# ============================================================
# USER HISTORY
# ============================================================

@app.route("/history")
def history():

    if not login_required():
        flash("Please login to view your history.", "error")
        return redirect(url_for("login"))

    conn = get_db()

    rows = conn.execute("""
        SELECT a.*,
               (
                    SELECT COUNT(*)
                    FROM farmer_responses fr
                    WHERE fr.analysis_id = a.id
                ) AS response_count
        FROM analyses a
        WHERE a.user_id = ?
        ORDER BY a.id DESC
    """, (session["user_id"],)).fetchall()

    conn.close()

    history_records = []

    for row in rows:
        item = dict(row)

        item["result"] = item.get("disease") or "Unknown"
        item["date"] = item.get("created_at") or "-"

        item["advice"] = (
            int(item.get("response_count") or 0) > 0
        )

        history_records.append(item)

    return render_template(
        "history.html",
        history=history_records,
        analyses=history_records,
        total_analyses=len(history_records)
    )


# ============================================================
# VIEW SAVED RESULT
# ============================================================

@app.route("/result/<int:analysis_id>", endpoint="result")
def view_result(analysis_id):

    if not login_required():
        return redirect(url_for("login"))

    conn = get_db()

    analysis = conn.execute("""
        SELECT a.*, u.name AS user_name, u.email AS user_email
        FROM analyses a
        JOIN users u ON a.user_id = u.id
        WHERE a.id = ?
    """, (analysis_id,)).fetchone()

    if not analysis:
        conn.close()
        return error_page("Analysis not found.", 404)

    if (
        session.get("role") == "user"
        and analysis["user_id"] != session.get("user_id")
    ):
        conn.close()
        return error_page(
            "You are not allowed to view this analysis.",
            403
        )

    responses = conn.execute("""
        SELECT *
        FROM farmer_responses
        WHERE analysis_id = ?
        ORDER BY id DESC
    """, (analysis_id,)).fetchall()

    conn.close()

    disease_info = {}

    if get_disease_info:
        try:
            disease_info = get_disease_info(
                analysis["disease"]
            ) or {}
        except Exception as exc:
            print("Disease information error:", repr(exc))

    advice = get_advice(
        analysis["disease"],
        analysis["growth_stage"]
    )

    saved_leaf_filename = (
        analysis["leaf_image_filename"]
        or analysis["image_filename"]
    )

    severity_result = get_severity_result(
        saved_leaf_filename
    )

    return render_template(
        "result.html",
        analysis=analysis,
        analysis_id=analysis["id"],
        image_filename=analysis["image_filename"],
        leaf_image_filename=analysis["leaf_image_filename"],
        stem_image_filename=analysis["stem_image_filename"],
        root_image_filename=analysis["root_image_filename"],
        whole_plant_image_filename=analysis["whole_plant_image_filename"],
        plant_part=analysis["plant_part"],
        disease=analysis["disease"],
        confidence=analysis["confidence"],
        plant_verified=analysis["plant_verified"],
        tomato_status=analysis["tomato_status"],
        symptoms=analysis["symptoms"],
        duration=analysis["duration"],
        growth_stage=analysis["growth_stage"],
        environment=analysis["environment"],
        disease_info=disease_info,

        # Complete advice for treatment/prevention cards.
       # Complete disease advice object.
advice=advice,

# Disease-specific treatment and prevention.
treatment=advice.get("application", []),
prevention=advice.get("prevention", []),
application=advice.get("application", []),
precautions=advice.get("precautions", []),

        # Severity result.
        affected_percentage=severity_result["affected_percentage"],
        remaining_percentage=severity_result["remaining_percentage"],
        severity_stage=severity_result["severity_stage"],
        severity_advice=severity_result["severity_advice"],
        severity_overlay=severity_result["severity_overlay"]
    )


# ============================================================
# FARMER DASHBOARD
# ============================================================

@app.route("/farmer/dashboard")
def farmer_dashboard():

    if not role_required("farmer"):
        flash("Farmer access required.", "error")
        return redirect(url_for("login"))

    conn = get_db()

    analyses = conn.execute("""
        SELECT a.*, u.name AS user_name, u.email AS user_email,
               (
                    SELECT COUNT(*)
                    FROM farmer_responses fr
                    WHERE fr.analysis_id = a.id
                ) AS response_count
        FROM analyses a
        JOIN users u ON a.user_id = u.id
        ORDER BY a.id DESC
    """).fetchall()

    total = conn.execute(
        "SELECT COUNT(*) FROM analyses"
    ).fetchone()[0]

    answered = conn.execute("""
        SELECT COUNT(DISTINCT analysis_id)
        FROM farmer_responses
    """).fetchone()[0]

    conn.close()

    return render_template(
        "farmer_dashboard.html",
        analyses=analyses,
        total=total,
        answered=answered,
        pending=total - answered
    )


@app.route(
    "/farmer/respond/<int:analysis_id>",
    methods=["POST"]
)
def farmer_response(analysis_id):

    if not role_required("farmer"):
        flash("Farmer access required.", "error")
        return redirect(url_for("login"))

    response_text = request.form.get(
        "farmer_response", ""
    ).strip()

    if not response_text:
        flash("Please write your farming advice.", "error")
        return redirect(url_for("farmer_dashboard"))

    conn = get_db()

    farmer = conn.execute("""
        SELECT *
        FROM users
        WHERE id = ? AND role = 'farmer'
    """, (session["user_id"],)).fetchone()

    analysis = conn.execute(
        "SELECT id FROM analyses WHERE id = ?",
        (analysis_id,)
    ).fetchone()

    if not farmer or not analysis:
        conn.close()
        flash("Farmer or analysis record not found.", "error")
        return redirect(url_for("farmer_dashboard"))

    conn.execute("""
        INSERT INTO farmer_responses (
            analysis_id, farmer_id, farmer_name, response
        )
        VALUES (?, ?, ?, ?)
    """, (
        analysis_id,
        farmer["id"],
        farmer["name"],
        response_text
    ))

    conn.commit()
    conn.close()

    flash(
        "Your farming advice has been sent successfully!",
        "success"
    )

    return redirect(url_for("farmer_dashboard"))


# ============================================================
# FARMER SUGGESTIONS
# ============================================================

@app.route("/farmer-suggestions")
def farmer_suggestions():

    if not login_required():
        return redirect(url_for("login"))

    return render_template("farmer_suggestions.html")


# ============================================================
# ADMIN DASHBOARD
# ============================================================

@app.route("/admin/dashboard")
def admin_dashboard():

    if not role_required("admin"):
        flash("Admin access required.", "error")
        return redirect(url_for("login"))

    conn = get_db()

    users = conn.execute("""
        SELECT *
        FROM users
        ORDER BY id DESC
    """).fetchall()

    analyses = conn.execute("""
        SELECT a.*, u.name AS user_name, u.email AS user_email
        FROM analyses a
        JOIN users u ON a.user_id = u.id
        ORDER BY a.id DESC
    """).fetchall()

    responses = conn.execute("""
        SELECT fr.*, a.disease, a.user_id, u.name AS user_name
        FROM farmer_responses fr
        JOIN analyses a ON fr.analysis_id = a.id
        JOIN users u ON a.user_id = u.id
        ORDER BY fr.id DESC
    """).fetchall()

    total_users = conn.execute("""
        SELECT COUNT(*)
        FROM users
        WHERE role = 'user'
    """).fetchone()[0]

    total_analyses = conn.execute(
        "SELECT COUNT(*) FROM analyses"
    ).fetchone()[0]

    total_responses = conn.execute(
        "SELECT COUNT(*) FROM farmer_responses"
    ).fetchone()[0]

    total_farmers = conn.execute("""
        SELECT COUNT(*)
        FROM users
        WHERE role = 'farmer'
    """).fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        users=users,
        analyses=analyses,
        responses=responses,
        total_users=total_users,
        total_analyses=total_analyses,
        total_responses=total_responses,
        total_farmers=total_farmers
    )


# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(413)
def file_too_large(error):

    return render_template(
        "error.html",
        message=(
            "Uploaded images are too large. "
            "Maximum total size is 40 MB."
        )
    ), 413


@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "error.html",
        message="The requested page was not found."
    ), 404


# ============================================================
# RUN APP
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("LEAFVISION AI")
    print("URL: http://127.0.0.1:5000")
    print()

    print("ADMIN LOGIN")
    print("Email: admin@leafvision.ai")
    print("Password: admin123")
    print()

    print("FARMER LOGIN")
    print("Email: farmer@leafvision.ai")
    print("Password: farmer123")
    print("=" * 60)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )
