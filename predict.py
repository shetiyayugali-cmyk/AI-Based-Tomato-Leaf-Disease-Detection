import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image


# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "model")

DISEASE_MODEL_PATH = os.path.join(
    MODEL_DIR,
    "tomato_model.keras"
)

VALIDATOR_MODEL_PATH = os.path.join(
    MODEL_DIR,
    "tomato_validator.keras"
)


# ============================================================
# CONFIGURATION
# ============================================================

IMAGE_SIZE = (224, 224)

# Tomato validation threshold
# A plant must have at least this confidence
# to be accepted as tomato.
VALIDATION_THRESHOLD = 85.0


# IMPORTANT:
# This assumes the validator is:
#
# class 0 = Other
# class 1 = Tomato
#
# If your training code used the opposite order,
# change the logic in validate_tomato().
# ============================================================


# ============================================================
# DISEASE CLASS NAMES
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
    "Tomato___healthy"
]


# ============================================================
# DISEASE INFORMATION
# ============================================================

DISEASE_INFO = {

    "Tomato___Bacterial_spot": {
        "name": "Bacterial Spot",
        "description": (
            "Bacterial spot causes small dark lesions on "
            "tomato leaves and may affect fruits."
        ),
        "treatment": (
            "Remove severely infected leaves, avoid overhead "
            "watering and maintain good air circulation."
        ),
        "prevention": (
            "Use disease-free seeds and avoid working with "
            "plants when leaves are wet."
        )
    },

    "Tomato___Early_blight": {
        "name": "Early Blight",
        "description": (
            "Early blight produces dark circular spots with "
            "concentric rings, usually on older leaves."
        ),
        "treatment": (
            "Remove infected leaves and apply an appropriate "
            "fungicide according to the product label."
        ),
        "prevention": (
            "Maintain good spacing, improve air circulation "
            "and avoid water splashing on leaves."
        )
    },

    "Tomato___Late_blight": {
        "name": "Late Blight",
        "description": (
            "Late blight causes large dark or water-soaked "
            "lesions on leaves."
        ),
        "treatment": (
            "Remove severely affected plant material and use "
            "an appropriate fungicide according to the label."
        ),
        "prevention": (
            "Avoid prolonged leaf wetness and provide good "
            "air circulation."
        )
    },

    "Tomato___Leaf_Mold": {
        "name": "Leaf Mold",
        "description": (
            "Leaf mold commonly produces yellow patches on "
            "the upper surface and mold growth underneath."
        ),
        "treatment": (
            "Improve ventilation, reduce humidity and remove "
            "badly affected leaves."
        ),
        "prevention": (
            "Avoid excessive humidity and provide sufficient "
            "spacing between plants."
        )
    },

    "Tomato___Septoria_leaf_spot": {
        "name": "Septoria Leaf Spot",
        "description": (
            "Septoria leaf spot produces small circular spots "
            "with pale centers and dark margins."
        ),
        "treatment": (
            "Remove infected leaves and improve air circulation. "
            "Use suitable fungicide when necessary."
        ),
        "prevention": (
            "Remove plant debris and avoid overhead watering."
        )
    },

    "Tomato___Spider_mites_Two_spotted_spider_mite": {
        "name": "Spider Mites",
        "description": (
            "Spider mites can cause yellowing, stippling and "
            "fine webbing on tomato leaves."
        ),
        "treatment": (
            "Wash foliage with water and use an appropriate "
            "mite-control treatment when required."
        ),
        "prevention": (
            "Regularly inspect leaves and maintain suitable "
            "plant growing conditions."
        )
    },

    "Tomato___Target_Spot": {
        "name": "Target Spot",
        "description": (
            "Target spot causes circular brown lesions that "
            "may develop concentric rings."
        ),
        "treatment": (
            "Remove affected leaves and improve plant "
            "ventilation."
        ),
        "prevention": (
            "Avoid excessive leaf moisture and maintain "
            "adequate plant spacing."
        )
    },

    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "name": "Tomato Yellow Leaf Curl Virus",
        "description": (
            "This viral disease can cause yellowing, curling "
            "and stunted growth."
        ),
        "treatment": (
            "Remove severely infected plants and control "
            "whitefly populations."
        ),
        "prevention": (
            "Use healthy seedlings and control insect vectors."
        )
    },

    "Tomato___Tomato_mosaic_virus": {
        "name": "Tomato Mosaic Virus",
        "description": (
            "Tomato mosaic virus can cause mottled leaves, "
            "distortion and reduced plant growth."
        ),
        "treatment": (
            "Remove infected plants and disinfect tools."
        ),
        "prevention": (
            "Use clean tools, healthy planting material and "
            "avoid mechanical transmission."
        )
    },

    "Tomato___healthy": {
        "name": "Healthy Tomato Plant",
        "description": (
            "The tomato leaf appears healthy according to "
            "the trained AI model."
        ),
        "treatment": (
            "No disease treatment is required."
        ),
        "prevention": (
            "Continue proper watering, nutrition, sunlight "
            "and regular monitoring."
        )
    }
}


# ============================================================
# MODEL VARIABLES
# ============================================================

disease_model = None
validator_model = None


# ============================================================
# LOAD MODELS
# ============================================================

print("=" * 60)
print("Loading LeafVision AI models...")
print("=" * 60)


if not os.path.exists(DISEASE_MODEL_PATH):
    raise FileNotFoundError(
        "Tomato disease model not found:\n"
        + DISEASE_MODEL_PATH
    )


if not os.path.exists(VALIDATOR_MODEL_PATH):
    raise FileNotFoundError(
        "Tomato validator model not found:\n"
        + VALIDATOR_MODEL_PATH
    )


try:

    disease_model = load_model(
        DISEASE_MODEL_PATH,
        compile=False
    )

    print("Disease model loaded:")
    print(DISEASE_MODEL_PATH)

except Exception as e:

    raise RuntimeError(
        "Could not load tomato disease model:\n"
        + str(e)
    )


try:

    validator_model = load_model(
        VALIDATOR_MODEL_PATH,
        compile=False
    )

    print("Validator model loaded:")
    print(VALIDATOR_MODEL_PATH)

except Exception as e:

    raise RuntimeError(
        "Could not load tomato validator model:\n"
        + str(e)
    )


print("=" * 60)


# ============================================================
# IMAGE PREPARATION
# ============================================================

def prepare_image(image_path):

    if not os.path.exists(image_path):

        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    image = Image.open(image_path)

    # Convert to RGB
    image = image.convert("RGB")

    # Resize
    image = image.resize(IMAGE_SIZE)

    # Convert to numpy
    image = np.asarray(
        image,
        dtype=np.float32
    )

    # Normalize
    image = image / 255.0

    # Add batch dimension
    image = np.expand_dims(
        image,
        axis=0
    )

    return image


# ============================================================
# SIGMOID FUNCTION
# ============================================================

def _sigmoid(x):

    x = np.clip(
        x,
        -50,
        50
    )

    return 1.0 / (
        1.0 + np.exp(-x)
    )


# ============================================================
# TOMATO VALIDATION
# ============================================================

def validate_tomato(image_path):

    image = prepare_image(
        image_path
    )

    raw = np.asarray(
        validator_model.predict(
            image,
            verbose=0
        )
    )

    print()
    print("-" * 60)
    print("TOMATO VALIDATION")
    print("-" * 60)

    print(
        "Raw validator output:",
        raw
    )

    # ========================================================
    # BINARY MODEL
    # ========================================================

    if raw.size == 1:

        probability = float(
            raw.reshape(-1)[0]
        )

        final_layer = (
            validator_model.layers[-1]
        )

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

        # If output is logits instead of sigmoid
        if activation_name != "sigmoid":

            probability = _sigmoid(
                probability
            )

        probability = float(
            np.clip(
                probability,
                0.0,
                1.0
            )
        )

        # Assumption:
        # sigmoid probability = Tomato
        tomato_confidence = (
            probability * 100.0
        )

        other_confidence = (
            (1.0 - probability) * 100.0
        )

    # ========================================================
    # TWO-CLASS MODEL
    # ========================================================

    else:

        probabilities = (
            raw.reshape(-1)
            .astype(float)
        )

        if len(probabilities) != 2:

            raise ValueError(
                "Validator model must output "
                "either 1 value or 2 values."
            )

        # Check whether values already look
        # like probabilities.
        probability_sum = float(
            probabilities.sum()
        )

        if (
            np.any(probabilities < 0)
            or
            abs(
                probability_sum - 1.0
            ) > 0.05
        ):

            exp_values = np.exp(
                probabilities
                - np.max(probabilities)
            )

            probabilities = (
                exp_values
                / exp_values.sum()
            )

        # IMPORTANT
        #
        # class 0 = OTHER
        # class 1 = TOMATO

        other_confidence = (
            float(probabilities[0])
            * 100.0
        )

        tomato_confidence = (
            float(probabilities[1])
            * 100.0
        )

    # ========================================================
    # STRICT VALIDATION
    # ========================================================

    if (
        tomato_confidence >=
        VALIDATION_THRESHOLD
        and
        tomato_confidence >
        other_confidence
    ):

        label = "tomato"
        is_tomato = True

    else:

        label = "other"
        is_tomato = False

    # ========================================================
    # PRINT
    # ========================================================

    print(
        f"Tomato confidence : "
        f"{tomato_confidence:.2f}%"
    )

    print(
        f"Other confidence  : "
        f"{other_confidence:.2f}%"
    )

    print(
        f"Threshold         : "
        f"{VALIDATION_THRESHOLD:.2f}%"
    )

    print(
        f"Validator result  : "
        f"{label.upper()}"
    )

    print("-" * 60)

    return {

        "label": label,

        "is_tomato": is_tomato,

        "confidence":
            tomato_confidence,

        "tomato_confidence":
            tomato_confidence,

        "other_confidence":
            other_confidence,

        "predictions": {

            "Tomato Plant":
                tomato_confidence,

            "Other Plant":
                other_confidence
        }
    }


# ============================================================
# DISEASE PREDICTION
# ============================================================

def predict_disease(image_path):

    # --------------------------------------------------------
    # FIRST: VERIFY TOMATO
    # --------------------------------------------------------

    validation = validate_tomato(
        image_path
    )

    # --------------------------------------------------------
    # STOP IF NOT TOMATO
    # --------------------------------------------------------

    if not validation["is_tomato"]:

        print()
        print("=" * 60)
        print("NOT A TOMATO PLANT")
        print("=" * 60)
        print(
            f"Tomato confidence: "
            f"{validation['tomato_confidence']:.2f}%"
        )
        print(
            f"Other confidence: "
            f"{validation['other_confidence']:.2f}%"
        )
        print("=" * 60)

        return {

            "disease": "Unsupported Plant",

            "label": "Unsupported Plant",

            "confidence":
                validation["confidence"],

            "is_tomato": False,

            "tomato_confidence":
                validation[
                    "tomato_confidence"
                ],

            "other_confidence":
                validation[
                    "other_confidence"
                ],

            "message": (
                "The uploaded image does not "
                "appear to be a tomato plant. "
                "Please upload a clear tomato "
                "leaf image."
            ),

            "predictions": {}
        }

    # --------------------------------------------------------
    # TOMATO CONFIRMED
    # --------------------------------------------------------

    image = prepare_image(
        image_path
    )

    raw_predictions = np.asarray(
        disease_model.predict(
            image,
            verbose=0
        )
    )

    probabilities = (
        raw_predictions.reshape(-1)
        .astype(float)
    )

    # --------------------------------------------------------
    # HANDLE MODEL OUTPUT
    # --------------------------------------------------------

    # If the model does not return
    # probabilities, apply softmax.
    probability_sum = float(
        probabilities.sum()
    )

    if (
        np.any(probabilities < 0)
        or
        abs(
            probability_sum - 1.0
        ) > 0.05
    ):

        exp_values = np.exp(
            probabilities
            - np.max(probabilities)
        )

        probabilities = (
            exp_values
            / exp_values.sum()
        )

    # --------------------------------------------------------
    # CLASS COUNT CHECK
    # --------------------------------------------------------

    if len(probabilities) != len(
        DISEASE_CLASSES
    ):

        raise ValueError(
            "Disease model returned "
            f"{len(probabilities)} classes, "
            "but predict.py contains "
            f"{len(DISEASE_CLASSES)} class names."
        )

    # --------------------------------------------------------
    # BEST PREDICTION
    # --------------------------------------------------------

    best_index = int(
        np.argmax(probabilities)
    )

    best_probability = float(
        probabilities[best_index]
    )

    disease_label = (
        DISEASE_CLASSES[best_index]
    )

    confidence = (
        best_probability * 100.0
    )

    # --------------------------------------------------------
    # GET INFORMATION
    # --------------------------------------------------------

    disease_info = get_disease_info(
        disease_label
    )

    print()
    print("=" * 60)
    print("DISEASE PREDICTION")
    print("=" * 60)

    print(
        "Disease:",
        disease_info["name"]
    )

    print(
        f"Confidence: {confidence:.2f}%"
    )

    print("=" * 60)

    # --------------------------------------------------------
    # RETURN RESULT
    # --------------------------------------------------------

    return {

        "disease":
            disease_info["name"],

        "label":
            disease_label,

        "confidence":
            confidence,

        "is_tomato":
            True,

        "tomato_confidence":
            validation[
                "tomato_confidence"
            ],

        "other_confidence":
            validation[
                "other_confidence"
            ],

        "description":
            disease_info[
                "description"
            ],

        "treatment":
            disease_info[
                "treatment"
            ],

        "prevention":
            disease_info[
                "prevention"
            ],

        "predictions": {

            DISEASE_CLASSES[i]:
                float(probabilities[i] * 100.0)

            for i in range(
                len(DISEASE_CLASSES)
            )
        }
    }


# ============================================================
# GET DISEASE INFORMATION
# ============================================================

def get_disease_info(
    disease_label
):

    # Direct match
    if disease_label in DISEASE_INFO:

        return DISEASE_INFO[
            disease_label
        ]

    # Try matching simplified name
    for key, info in DISEASE_INFO.items():

        if (
            disease_label.lower()
            in key.lower()
        ):

            return info

    # Unknown disease
    return {

        "name":
            disease_label.replace(
                "Tomato___",
                ""
            ).replace(
                "_",
                " "
            ),

        "description":
            "The AI model detected a tomato plant condition.",

        "treatment":
            "Consult an agricultural expert for appropriate treatment.",

        "prevention":
            "Maintain proper plant hygiene, watering and monitoring."
    }


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("LeafVision AI prediction module")
    print("=" * 60)

    print(
        "Disease model:",
        DISEASE_MODEL_PATH
    )

    print(
        "Validator model:",
        VALIDATOR_MODEL_PATH
    )

    print()
    print("Module loaded successfully.")
    print(
        "Use predict_disease(image_path) "
        "to make a prediction."
    )