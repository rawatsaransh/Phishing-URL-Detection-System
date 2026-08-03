def calculate_score(analysis_data):
    score = 0

    if not analysis_data["uses_https"]:
        score += 1
    if analysis_data["is_long_url"]:
        score += 1
    if analysis_data["contains_at_symbol"]:
        score += 2
    if analysis_data["many_subdomains"]:
        score += 2
    if analysis_data["contains_ip_address"]:
        score += 4

    if not analysis_data["valid_ssl"]:
        score += 2

    domain_age = analysis_data["domain_age"]
    if domain_age is not None:
        if domain_age < 30:
            score += 3
        elif domain_age < 180 :
            score += 1

    if not analysis_data["valid_dns"]:
        score += 1

    malicious = analysis_data["malicious"]
    if malicious is not None:
        if 1 <= malicious <= 2:
            score += 5
        elif 3 <= malicious <= 5:
            score += 10
        elif malicious > 5:
            score += 20

    suspicious = analysis_data["suspicious"]
    if suspicious is not None:
        if 1 <= suspicious <= 2:
            score += 3
        elif suspicious > 2:
            score += 5

    return score


def calculate_risk(score):

    if score <= 5:
        return "🟢 LOW"

    elif score <= 15:
        return "🟡 MEDIUM"

    else:
        return "🔴 HIGH"


