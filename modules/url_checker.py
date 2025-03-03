import re

def is_suspicious_url(url):
    """Detect phishing patterns in the URL using regex."""
    phishing_patterns = [
        r"https?:\/\/.*@.*",  # Detects "@" symbol trick (e.g., google.com-redirect@valimail.com)
        r"https?:\/\/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+",  # IP-based URL
        r"https?:\/\/.*(free|cheap|bonus|login|secure|verify|bank|paypal).*",  # Suspicious words
        r"https?:\/\/.*\.(xyz|top|click|gq|tk|ml|cf|ga).*",  # Unusual TLDs
        r"https?:\/\/(www\.)?([a-zA-Z0-9-]+)\.\2",  # Typosquatting (e.g., go0gle.com)
        r"https?:\/\/.*(bit\.ly|tinyurl\.com|t\.co|shorturl\.at).*",  # Shortened links
        r"https?:\/\/.*[.-]{2,}.*",  # Detects unusual domain names with consecutive periods or dashes
        r"https?:\/\/.*-.*@.*",  # Detect URL redirect patterns or special characters
        r"https?:\/\/.*\b[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}\b",  # Email-like structure in URL
    ]
    return any(re.search(pattern, url) for pattern in phishing_patterns)

def has_redirect_pattern(url):
    """Check if the URL contains suspicious redirect patterns using @ symbol."""
    return bool(re.search(r".*-.*@.*", url))
