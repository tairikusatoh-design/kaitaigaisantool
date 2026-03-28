def calculate_estimate(data):
    area = float(data.get("area", 0))
    floors = int(data.get("floors", 1))

    base = area * 14500
    floor_coef = 1 + (floors - 1) * 0.5
    
def get_reasons(data):
    year = int(data.get("year", 30))

    reasons = []

    if year >= 40:
        reasons.append("築年数が古く、現在と異なる施工方法が使われている可能性があります")
        reasons.append("材料や下地構成により、解体手間が増える想定です")
        reasons.append("古い建物特有の構造により、作業効率が低下する可能性があります")

    elif year >= 20:
        reasons.append("築年数により使用材料や施工方法に差が出やすい年代です")
        reasons.append("一部で解体手間が増える可能性があります")

    else:
        reasons.append("比較的新しい施工が想定されます")
        reasons.append("材料構成により作業効率が変動する可能性があります")

    return reasons[:3]
