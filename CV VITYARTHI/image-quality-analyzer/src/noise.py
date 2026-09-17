import cv2
import numpy as np


def estimate_noise(image):
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    filtered = cv2.medianBlur(
        gray,
        3
    )

    difference = cv2.absdiff(
        gray,
        filtered
    )

    return float(np.mean(difference))
