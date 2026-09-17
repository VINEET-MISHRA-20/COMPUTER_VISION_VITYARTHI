import sys
from pathlib import Path

# Add the project root to Python's import path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import cv2
import numpy as np
import pytest

from src.analyzer import analyze_image


def test_analyze_image(tmp_path):
    image = np.full((200, 200, 3), 128, dtype=np.uint8)

    image_path = tmp_path / "test.jpg"
    cv2.imwrite(str(image_path), image)

    result = analyze_image(str(image_path))

    assert isinstance(result, dict)

    # Basic result structure
    assert "file" in result
    assert "resolution" in result
    assert "metrics" in result
    assert "scores" in result

    # Image-quality measurements
    assert "brightness" in result["metrics"]
    assert "contrast" in result["metrics"]
    assert "sharpness" in result["metrics"]
    assert "noise" in result["metrics"]

    # Component scores and overall quality score
    assert "brightness" in result["scores"]
    assert "contrast" in result["scores"]
    assert "sharpness" in result["scores"]
    assert "noise" in result["scores"]
    assert "overall" in result["scores"]

    # Quality classification
    assert "label" in result
    assert isinstance(result["scores"]["overall"], (int, float))
    assert isinstance(result["label"], str)


def test_missing_image():
    with pytest.raises(ValueError, match="Could not read image"):
        analyze_image("does_not_exist.jpg")
