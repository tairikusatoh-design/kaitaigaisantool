def calculate_estimate(data):
    area = float(data.get("area", 0))
    floors = int(data.get("floors", 1))

    base = area * 14500
    floor_coef = 1 + (floors - 1) * 0.5

    detail = int(base * floor_coef)

    return {
        "min": int(detail * 0.85),
        "max": int(detail * 1.15),
        "detail": detail
    }


def get_reasons(data):
    reasons = []

    hand = int(data.get("hand", 0))
    space = data.get("space", "normal")

    if hand >= 40:
        reasons.append("手解体割合が高く、人工作業が増える想定です")

    if space == "narrow":
        reasons.append("作業スペースが限られ、作業効率が低下する想定です")

    if len(reasons) == 0:
        reasons.append("一般的な作業条件での想定です")

    return reasons[:3]
