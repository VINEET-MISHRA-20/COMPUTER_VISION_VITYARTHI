def brightness_quality(value):
    score = 1 - abs(value - 128) / 128
    return max(0, min(1, score))


def contrast_quality(value):
    score = value / 80
    return max(0, min(1, score))


def sharpness_quality(value):
    score = value / 500
    return max(0, min(1, score))


def noise_quality(value):
    score = 1 - value / 30
    return max(0, min(1, score))


def calculate_overall_score(scores):
    total = (
        scores["brightness"] * 0.25
        + scores["contrast"] * 0.25
        + scores["sharpness"] * 0.30
        + scores["noise"] * 0.20
    )

    return round(total * 100, 2)


def classify_quality(score):
    if score >= 80:
        return "Excellent"

    if score >= 60:
        return "Good"

    if score >= 40:
        return "Fair"

    return "Poor"
