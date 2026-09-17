from pathlib import Path

import cv2

from src.brightness import calculate_brightness
from src.contrast import calculate_contrast
from src.sharpness import calculate_sharpness
from src.noise import estimate_noise

from src.scoring import (
    brightness_quality,
    contrast_quality,
    sharpness_quality,
    noise_quality,
    calculate_overall_score,
    classify_quality
)


SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff"
}


def generate_recommendations(metrics):
    recommendations = []

    if metrics["brightness"] < 60:
        recommendations.append(
            "Image may be too dark. Consider increasing exposure."
        )

    elif metrics["brightness"] > 195:
        recommendations.append(
            "Image may be too bright. Consider reducing exposure."
        )

    if metrics["contrast"] < 25:
        recommendations.append(
            "Low contrast detected."
        )

    if metrics["sharpness"] < 100:
        recommendations.append(
            "Low sharpness detected. Check focus or camera movement."
        )

    if metrics["noise"] > 10:
        recommendations.append(
            "High noise detected. Consider better lighting or denoising."
        )

    if not recommendations:
        recommendations.append(
            "No major quality problem detected."
        )

    return recommendations


def analyze_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            f"Could not read image: {image_path}"
        )

    height, width = image.shape[:2]

    brightness = calculate_brightness(image)
    contrast = calculate_contrast(image)
    sharpness = calculate_sharpness(image)
    noise = estimate_noise(image)

    metrics = {
        "brightness": round(brightness, 2),
        "contrast": round(contrast, 2),
        "sharpness": round(sharpness, 2),
        "noise": round(noise, 2)
    }

    scores = {
        "brightness": brightness_quality(brightness),
        "contrast": contrast_quality(contrast),
        "sharpness": sharpness_quality(sharpness),
        "noise": noise_quality(noise)
    }

    overall = calculate_overall_score(scores)

    return {
        "file": image_path,
        "resolution": {
            "width": width,
            "height": height
        },
        "metrics": metrics,
        "scores": {
            "brightness": round(scores["brightness"], 4),
            "contrast": round(scores["contrast"], 4),
            "sharpness": round(scores["sharpness"], 4),
            "noise": round(scores["noise"], 4),
            "overall": overall
        },
        "label": classify_quality(overall),
        "recommendations": generate_recommendations(metrics)
    }


def analyze_folder(folder_path):
    folder = Path(folder_path)
    results = []

    for path in sorted(folder.rglob("*")):
        if (
            path.is_file()
            and path.suffix.lower() in SUPPORTED_EXTENSIONS
        ):
            try:
                result = analyze_image(str(path))
                results.append(result)

            except Exception as error:
                print(
                    f"WARNING: Skipped {path}: {error}"
                )

    return results
