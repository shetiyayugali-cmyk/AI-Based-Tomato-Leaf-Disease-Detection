
import os
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


# ============================================================
# PATHS AND SETTINGS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

DISEASE_MODEL_PATH = os.path.join(
    MODEL_DIR, "tomato_model.keras"
)

VALIDATOR_MODEL_PATH = os.path.join(
    MODEL_DIR, "tomato_validator.keras"
)

IMAGE_SIZE = (224, 224)

# ============================================================
# MODEL CONFIGURATION
# ============================================================

# Minimum tomato validation confidence.
VALIDATION_THRESHOLD = 85.0

# Minimum disease prediction confidence.
MIN_DISEASE_CONFIDENCE = 75.0

# IMPORTANT:
# True  = higher sigmoid output means Tomato.
# False = higher sigmoid output means Other.
#
# Confirm this setting using your validator training labels.
VALIDATOR_TOMATO_OUTPUT_IS_HIGH = True


# ============================================================
# TOMATO DISEASE CLASSES
# Keep this order identical to model training order.
# ============================================================

DISEASE_CLASSES = [
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites_Two_spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]


# ============================================================
# DISEASE INFORMATION
# ============================================================

DISEASE_INFO = {

    "Tomato___Bacterial_spot": {
        "name": "Bacterial Spot",
        "description": (
            "Small dark lesions can appear on tomato leaves "
            "and may also affect fruits."
        ),
        "treatment": (
            "Remove severely infected leaves, avoid overhead "
            "watering, and seek local agricultural advice."
        ),
        "prevention": (
            "Use disease-free seeds, clean tools, and avoid "
            "working with plants while leaves are wet."
        )
    },

    "Tomato___Early_blight": {
        "name": "Early Blight",
        "description": (
            "Dark circular spots with concentric rings often "
            "appear on older leaves."
        ),
        "treatment": (
            "Remove infected leaves and use an appropriate "
            "fungicide only according to its label."
        ),
        "prevention": (
            "Maintain plant spacing, improve air circulation, "
            "and avoid splashing water onto leaves."
        )
    },

    "Tomato___Late_blight": {
        "name": "Late Blight",
        "description": (
            "Large dark or water-soaked lesions can develop "
            "on tomato leaves."
        ),
        "treatment": (
            "Remove severely affected plant material safely "
            "and seek local agricultural guidance."
        ),
        "prevention": (
            "Reduce prolonged leaf wetness and provide "
            "good air circulation."
        )
    },

    "Tomato___Leaf_Mold": {
        "name": "Leaf Mold",
        "description": (
            "Yellow patches may appear on the upper leaf "
            "surface with mold growth underneath."
        ),
        "treatment": (
            "Improve ventilation, reduce humidity, and "
            "remove badly affected leaves."
        ),
        "prevention": (
            "Avoid excessive humidity and provide adequate "
            "spacing between plants."
        )
    },

    "Tomato___Septoria_leaf_spot": {
        "name": "Septoria Leaf Spot",
        "description": (
            "Small circular spots with pale centers and "
            "dark margins may develop on leaves."
        ),
        "treatment": (
            "Remove infected leaves and improve air circulation. "
            "Use suitable treatment only when advised."
        ),
        "prevention": (
            "Remove plant debris and avoid overhead watering."
        )
    },

    "Tomato___Spider_mites_Two_spotted_spider_mite": {
        "name": "Spider Mites",
        "description": (
            "Spider mites may cause yellow stippling and "
            "fine webbing on tomato leaves."
        ),
        "treatment": (
            "Inspect the undersides of leaves and use an "
            "appropriate mite-control method as directed."
        ),
        "prevention": (
            "Inspect plants regularly and maintain suitable "
            "growing conditions."
        )
    },

    "Tomato___Target_Spot": {
        "name": "Target Spot",
        "description": (
            "Circular brown lesions may develop concentric "
            "rings on affected leaves."
        ),
        "treatment": (
            "Remove affected leaves and improve plant ventilation."
        ),
        "prevention": (
            "Avoid excessive leaf moisture and maintain "
            "adequate plant spacing."
        )
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "name": "Tomato Yellow Leaf Curl Virus",
        "description": (
            "Symptoms can include yellowing, curling leaves, "
            "and stunted plant growth."
        ),
        "treatment": (
            "Seek local agricultural advice and manage "
            "whiteflies using appropriate methods."
        ),
        "prevention": (
            "Use healthy seedlings and monitor insect vectors."
        )
    },

    "Tomato___Tomato_mosaic_virus": {
        "name": "Tomato Mosaic Virus",
        "description": (
            "Mottled, distorted leaves and reduced growth "
            "may indicate tomato mosaic virus."
        ),
        "treatment": (
            "Remove infected plants when confirmed and "
            "disinfect tools appropriately."
        ),
        "prevention": (
            "Use healthy planting material, clean tools, "
            "and avoid mechanical transmission."
        )
    },

    "Tomato___healthy": {
        "name": "Healthy Tomato Plant",
        "description": (
            "The image appears consistent with a healthy "
            "tomato leaf according to the AI model."
        ),
        "treatment": "No disease treatment is indicated.",
        "prevention": (
            "Continue proper watering, nutrition, sunlight, "
            "and regular plant monitoring."
        )
    }
}


# ============================================================
# LOAD MODELS
# ============================================================

print("\nLoading LeafVision AI models...")

if not os.path.isfile(DISEASE_MODEL_PATH):
    raise FileNotFoundError(
        f"Tomato disease model not found: {DISEASE_MODEL_PATH}"
    )

if not os.path.isfile(VALIDATOR_MODEL_PATH):
    raise FileNotFoundError(
        f"Tomato validator model not found: {VALIDATOR_MODEL_PATH}"
    )

try:
    disease_model = load_model(
        DISEASE_MODEL_PATH,
        compile=False
    )

    validator_model = load_model(
        VALIDATOR_MODEL_PATH,
        compile=False
    )

except Exception as exc:
    raise RuntimeError(
        f"Unable to load LeafVision AI models: {exc}"
    ) from exc

print("Disease model loaded successfully.")
print("Tomato validator loaded successfully.")
print("Disease model output shape:", disease_model.output_shape)
print("Validator model output shape:", validator_model.output_shape)


# ============================================================
# IMAGE PREPARATION
# ============================================================

def prepare_image(image_path):

    if not os.path.isfile(image_path):
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    try:
        with Image.open(image_path) as source:
            image = source.convert("RGB")
            image = image.resize(IMAGE_SIZE)

            array = np.asarray(
                image,
                dtype=np.float32
            )

    except Exception as exc:
        raise ValueError(
            "The uploaded file is not a valid image."
        ) from exc

    # IMPORTANT:
    # This preprocessing must match your model training.
    array = array / 255.0

    return np.expand_dims(array, axis=0)


# ============================================================
# DISEASE INFORMATION
# ============================================================

def get_disease_info(disease_label):

    if disease_label in DISEASE_INFO:
        return DISEASE_INFO[disease_label]

    simplified = str(disease_label).replace(
        "Tomato___", ""
    ).replace("_", " ")

    for key, info in DISEASE_INFO.items():

        if simplified.lower() == info["name"].lower():
            return info

    return {
        "name": simplified,
        "description": "Disease information is not available.",
        "treatment": "Consult an agricultural expert.",
        "prevention": (
            "Maintain plant hygiene and monitor the plant."
        )
    }


# ============================================================
# UNSUPPORTED IMAGE RESPONSE
# ============================================================

def unsupported_result(
    tomato_confidence=0.0,
    other_confidence=100.0,
    message=None,
    predictions=None
):

    return {
        "disease": "Unsupported Plant",
        "label": "Unsupported Plant",
        "confidence": 0.0,
        "is_tomato": False,

        "tomato_confidence": float(tomato_confidence),
        "other_confidence": float(other_confidence),

        "message": message or (
            "This image could not be verified as a tomato leaf. "
            "Please upload a clear tomato leaf image."
        ),

        "predictions": predictions or {}
    }


# ============================================================
# SIGMOID HELPER
# ============================================================

def sigmoid(value):

    value = np.clip(value, -50, 50)

    return 1.0 / (1.0 + np.exp(-value))


# ============================================================
# TOMATO VALIDATION
# ============================================================

def validate_tomato(image_path):
    """
    Validates whether the uploaded image is a tomato image.

    The validator must have one sigmoid/logit output.

    VALIDATOR_TOMATO_OUTPUT_IS_HIGH controls the meaning
    of the output according to the training class labels.
    """

    image = prepare_image(image_path)

    raw = np.asarray(
        validator_model.predict(
            image,
            verbose=0
        )
    ).reshape(-1)

    print("\n" + "=" * 55)
    print("LEAFVISION TOMATO VALIDATION")
    print("=" * 55)

    print("Image:", image_path)
    print("Validator model:", VALIDATOR_MODEL_PATH)
    print("Raw validator output:", raw)

    if raw.size != 1:
        raise ValueError(
            "The tomato validator must return exactly one output. "
            f"Received {raw.size} outputs. Check model architecture."
        )

    output = float(raw[0])

    if not np.isfinite(output):
        raise ValueError(
            "Validator returned an invalid numeric value."
        )

    # Determine whether the model returns a probability or logit.
    final_layer = validator_model.layers[-1]

    activation = getattr(
        final_layer,
        "activation",
        None
    )

    activation_name = getattr(
        activation,
        "__name__",
        ""
    )

    if activation_name == "sigmoid":
        probability = output

    elif 0.0 <= output <= 1.0:
        probability = output

    else:
        # Convert a logit into a probability.
        probability = float(sigmoid(output))

    if not 0.0 <= probability <= 1.0:
        raise ValueError(
            "Invalid validator probability. "
            "Check the final model activation."
        )

    # Set the class interpretation according to training labels.
    if VALIDATOR_TOMATO_OUTPUT_IS_HIGH:

        tomato_probability = probability

    else:

        tomato_probability = 1.0 - probability

    tomato_confidence = tomato_probability * 100.0

    other_confidence = (
        1.0 - tomato_probability
    ) * 100.0

    is_tomato = (
        tomato_confidence >= VALIDATION_THRESHOLD
    )

    result = {
        "label": "tomato" if is_tomato else "other",

        "is_tomato": is_tomato,

        "confidence": tomato_confidence,

        "tomato_confidence": tomato_confidence,

        "other_confidence": other_confidence,

        "raw_output": output,

        "probability": probability,

        "predictions": {
            "Tomato Plant": tomato_confidence,
            "Other Plant": other_confidence
        }
    }

    print("-" * 55)
    print("Raw output:", round(output, 6))
    print("Activation:", activation_name)
    print("Tomato output mapping:", VALIDATOR_TOMATO_OUTPUT_IS_HIGH)
    print("Tomato confidence:", round(tomato_confidence, 2), "%")
    print("Other confidence:", round(other_confidence, 2), "%")
    print("Required threshold:", VALIDATION_THRESHOLD, "%")
    print("Validation result:", result["label"])
    print("=" * 55 + "\n")

    return result


# ============================================================
# DISEASE PROBABILITY CONVERSION
# ============================================================

def convert_to_probabilities(raw):

    raw = np.asarray(
        raw,
        dtype=np.float64
    ).reshape(-1)

    if not np.all(np.isfinite(raw)):
        raise ValueError(
            "Disease model returned invalid values."
        )

    if len(raw) != len(DISEASE_CLASSES):
        raise ValueError(
            f"Disease model returned {len(raw)} outputs, "
            f"but {len(DISEASE_CLASSES)} classes are configured."
        )

    total = float(np.sum(raw))

    # Already normalized probability output.
    if (
        np.all(raw >= 0)
        and np.all(raw <= 1)
        and np.isclose(total, 1.0, atol=0.05)
    ):

        return raw / total

    # Convert logits or non-normalized outputs using softmax.
    shifted = raw - np.max(raw)

    exp_values = np.exp(shifted)

    probabilities = (
        exp_values / np.sum(exp_values)
    )

    return probabilities


# ============================================================
# DISEASE PREDICTION
# ============================================================

def predict_disease(image_path):
    """
    Step 1: Validate tomato image.
    Step 2: Reject failed tomato validation.
    Step 3: Run 10-class disease classifier.
    Step 4: Check disease confidence.
    Step 5: Return prediction.
    """

    # --------------------------------------------------------
    # STEP 1: TOMATO VALIDATION
    # --------------------------------------------------------

    validation = validate_tomato(image_path)

    tomato_confidence = validation["tomato_confidence"]
    other_confidence = validation["other_confidence"]

    if not validation["is_tomato"]:

        print("Tomato validation failed.")
        print("Disease prediction will not run.")

        return unsupported_result(
            tomato_confidence=tomato_confidence,
            other_confidence=other_confidence,
            message=(
                "The uploaded image could not be verified "
                "as a tomato leaf. Please upload a clear "
                "tomato leaf image."
            )
        )

    # --------------------------------------------------------
    # STEP 2: DISEASE MODEL PREDICTION
    # --------------------------------------------------------

    print("\nRunning tomato disease classifier...")

    image = prepare_image(image_path)

    raw = np.asarray(
        disease_model.predict(
            image,
            verbose=0
        )
    ).reshape(-1)

    print("Raw disease predictions:", raw)

    probabilities = convert_to_probabilities(raw)

    # --------------------------------------------------------
    # STEP 3: FIND HIGHEST CONFIDENCE CLASS
    # --------------------------------------------------------

    best_index = int(
        np.argmax(probabilities)
    )

    confidence = float(
        probabilities[best_index] * 100.0
    )

    disease_label = DISEASE_CLASSES[best_index]

    predictions = {
        DISEASE_CLASSES[i]: float(
            probabilities[i] * 100.0
        )
        for i in range(len(DISEASE_CLASSES))
    }

    print("\n" + "=" * 55)
    print("TOMATO DISEASE PREDICTION")
    print("=" * 55)

    print("Predicted disease:", disease_label)
    print("Disease confidence:", round(confidence, 2), "%")
    print("Minimum confidence:", MIN_DISEASE_CONFIDENCE, "%")

    # --------------------------------------------------------
    # STEP 4: DISEASE CONFIDENCE CHECK
    # --------------------------------------------------------

    if confidence < MIN_DISEASE_CONFIDENCE:

        print("Disease confidence is below threshold.")
        print("Returning uncertain prediction.")

        return {
            "disease": "Uncertain Prediction",
            "label": "Uncertain Prediction",
            "confidence": confidence,
            "is_tomato": True,
            "tomato_confidence": tomato_confidence,
            "other_confidence": other_confidence,
            "message": (
                "The uploaded image appears to be a tomato "
                "leaf, but the disease could not be identified "
                "confidently. Please upload a clearer image."
            ),
            "predictions": predictions
        }

    # --------------------------------------------------------
    # STEP 5: GET DISEASE INFORMATION
    # --------------------------------------------------------

    info = get_disease_info(disease_label)

    print("Final disease:", info["name"])
    print("=" * 55 + "\n")

    return {
        "disease": info["name"],

        "label": disease_label,

        "confidence": confidence,

        "is_tomato": True,

        "tomato_confidence": tomato_confidence,

        "other_confidence": other_confidence,

        "description": info["description"],

        "treatment": info["treatment"],

        "prevention": info["prevention"],

        "predictions": predictions
    }


# ============================================================
# COMPATIBILITY FUNCTIONS
# ============================================================

def validate_tomato_plant(image_path):

    return validate_tomato(image_path)


def predict(image_path):

    return predict_disease(image_path)


# ============================================================
# TEST MODULE
# ============================================================

if __name__ == "__main__":

    print("\nLEAFVISION AI - MODEL TEST")

    print("Disease model:", DISEASE_MODEL_PATH)
    print("Validator model:", VALIDATOR_MODEL_PATH)

    print("Image size:", IMAGE_SIZE)

    print("Tomato threshold:", VALIDATION_THRESHOLD)

    print(
        "Disease confidence threshold:",
        MIN_DISEASE_CONFIDENCE
    )

    print(
        "Tomato output mapping:",
        VALIDATOR_TOMATO_OUTPUT_IS_HIGH
    )

    print("\nAvailable disease classes:")

    for index, disease in enumerate(DISEASE_CLASSES, start=1):

        print(f"{index}. {disease}")

    print("\nLeafVision AI models are ready.")
