import cv2
import numpy as np


def calculate_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    laplacian = cv2.Laplacian(
        gray,
        cv2.CV_64F
    )

    return float(np.var(laplacian))
