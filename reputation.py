import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_reputation(domain):
    try:
        api_url = f"https://www.virustotal.com/api/v3/domains/{domain}"
        api_key = os.getenv("VT_API_KEY")

        if not api_key:
            return False, None, None, None, "API_KEY_NOT_FOUND"

        headers = {"x-apikey": api_key}
        response = requests.get(api_url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()

            stats = data['data']['attributes']['last_analysis_stats']
            malicious = stats['malicious']
            suspicious = stats['suspicious']
            harmless = stats['harmless']
            return True, malicious, suspicious, harmless, None

        elif response.status_code == 401:
            return False, None, None, None, "INVALID_API_KEY"

        elif response.status_code == 404:
            return False, None, None, None, "NOT_FOUND_IN_VIRUSTOTAL"

        elif response.status_code == 429:
            return False,None, None, None, "RATE_LIMIT_EXCEEDED"

        else:
            return False,None, None, None, "UNKNOWN_HTTP_ERROR"

    except requests.exceptions.Timeout:
        return False, None, None, None, "REQUEST_TIMEOUT"

    except requests.exceptions.RequestException as e:
        return False, None, None, None, str(e)
