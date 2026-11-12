
import cv2
import numpy as np
import base64


def analyze_leaf_severity(image_path):

    # ========================================================
    # STEP 1: READ IMAGE
    # ========================================================

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read the uploaded leaf image.")

    # Resize large images for faster processing
    height, width = image.shape[:2]

    scale = min(1.0, 800 / max(height, width))

    if scale < 1:
        image = cv2.resize(
            image,
            (
                int(width * scale),
                int(height * scale)
            ),
            interpolation=cv2.INTER_AREA
        )

    height, width = image.shape[:2]

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # ========================================================
    # STEP 2: DETECT LEAF AREA
    # ========================================================

    mask = np.zeros((height, width), np.uint8)

    rect = (
        int(width * 0.03),
        int(height * 0.03),
        int(width * 0.94),
        int(height * 0.94)
    )

    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    try:
        cv2.grabCut(
            image,
            mask,
            rect,
            background_model,
            foreground_model,
            5,
            cv2.GC_INIT_WITH_RECT
        )
    except cv2.error as exc:
        raise ValueError(
            "Unable to identify the leaf area. "
            "Please upload a clear leaf image."
        ) from exc

    leaf_mask = np.where(
        (mask == cv2.GC_FGD) |
        (mask == cv2.GC_PR_FGD),
        255,
        0
    ).astype(np.uint8)

    contours, _ = cv2.findContours(
        leaf_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        raise ValueError("Leaf area could not be detected.")

    # Select the largest detected region
    largest_contour = max(
        contours,
        key=cv2.contourArea
    )

    clean_leaf_mask = np.zeros_like(leaf_mask)

    cv2.drawContours(
        clean_leaf_mask,
        [largest_contour],
        -1,
        255,
        thickness=cv2.FILLED
    )

    total_leaf_pixels = cv2.countNonZero(
        clean_leaf_mask
    )

    if total_leaf_pixels < 500:
        raise ValueError(
            "Insufficient leaf area detected. "
            "Please upload a clearer image."
        )

    # ========================================================
    # STEP 3: DETECT VISIBLY DISCOLOURED AREAS
    # ========================================================

    # Brown regions
    brown_mask = cv2.inRange(
        hsv,
        np.array([5, 45, 20]),
        np.array([25, 255, 210])
    )

    # Yellow regions
    yellow_mask = cv2.inRange(
        hsv,
        np.array([18, 45, 70]),
        np.array([40, 255, 255])
    )

    # Very dark regions
    dark_mask = cv2.inRange(
        hsv,
        np.array([0, 35, 0]),
        np.array([179, 255, 45])
    )

    # Combine detected colour regions
    damaged_mask = cv2.bitwise_or(
        brown_mask,
        yellow_mask
    )

    damaged_mask = cv2.bitwise_or(
        damaged_mask,
        dark_mask
    )

    # Count only regions inside the detected leaf
    damaged_mask = cv2.bitwise_and(
        damaged_mask,
        clean_leaf_mask
    )

    # Remove small noise
    kernel = np.ones((3, 3), np.uint8)

    damaged_mask = cv2.morphologyEx(
        damaged_mask,
        cv2.MORPH_OPEN,
        kernel
    )

    # ========================================================
    # STEP 4: CALCULATE AFFECTED AND REMAINING PERCENTAGE
    # ========================================================

    damaged_pixels = cv2.countNonZero(
        damaged_mask
    )

    affected_percentage = (
        damaged_pixels / total_leaf_pixels
    ) * 100

    affected_percentage = round(
        min(100.0, max(0.0, affected_percentage)),
        2
    )

    remaining_percentage = round(
        100.0 - affected_percentage,
        2
    )

    # ========================================================
    # STEP 5: ESTIMATE DISEASE SEVERITY STAGE
    # ========================================================

    if affected_percentage <= 20:

        stage = "Early Stage"

        advice = (
            "The estimated affected area is low. "
            "Monitor the leaf regularly and inspect "
            "nearby leaves for similar symptoms."
        )

    elif affected_percentage <= 50:

        stage = "Moderate Stage"

        advice = (
            "The estimated affected area is moderate. "
            "Inspect the plant carefully and follow "
            "appropriate disease-management guidance."
        )

    else:

        stage = "Severe Stage"

        advice = (
            "The estimated affected area is high. "
            "Inspect the entire plant and seek advice "
            "from an agricultural expert."
        )

    # ========================================================
    # STEP 6: GENERATE HIGHLIGHTED DAMAGE OVERLAY
    # ========================================================

    overlay = image.copy()

    # Highlight detected damaged regions in red
    overlay[damaged_mask > 0] = (0, 0, 255)

    result_image = cv2.addWeighted(
        image,
        0.65,
        overlay,
        0.35,
        0
    )

    success, encoded_image = cv2.imencode(
        ".jpg",
        result_image
    )

    if not success:
        raise ValueError(
            "Unable to generate severity overlay."
        )

    overlay_base64 = base64.b64encode(
        encoded_image.tobytes()
    ).decode("utf-8")

    # ========================================================
    # STEP 7: RETURN ALL RESULTS
    # ========================================================

    return {
        "affected_percentage": affected_percentage,
        "remaining_percentage": remaining_percentage,
        "severity_stage": stage,
        "severity_advice": advice,
        "severity_overlay": overlay_base64
    }
