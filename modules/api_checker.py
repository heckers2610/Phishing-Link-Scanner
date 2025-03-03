import requests

GOOGLE_API_KEY = "your_google_api_key"  # Replace with your actual API Key

def check_google_safe_browsing(url):
    """Check if a URL is blacklisted by Google Safe Browsing API."""
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={GOOGLE_API_KEY}"
    payload = {
        "client": {"clientId": "phishing-scanner", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        },
    }
    try:
        response = requests.post(api_url, json=payload)
        result = response.json()
        return "matches" in result  # If URL is found in the database, it's phishing
    except requests.RequestException:
        return False  # If there's an error, assume it's safe (or handle it differently)
