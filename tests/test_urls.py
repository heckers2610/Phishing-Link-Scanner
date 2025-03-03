from modules.url_checker import is_suspicious_url, has_redirect_pattern
from modules.api_checker import check_google_safe_browsing

# Test URLs
test_urls = [
    "http://example.com@malicious.com",  # Phishing pattern
    "http://192.168.1.1",  # IP-based URL
    "http://free-money.xyz",  # Suspicious TLD
    "http://secure-login.paypal.com.scam-site.com",  # Typo-squatting
    "http://bit.ly/phishy",  # Shortened link
    "https://www.google.com",  # Safe URL
    "https://github.com",  # Safe URL
]

print("\n🔍 Running Tests for URL Scanner...\n")

for url in test_urls:
    print(f"Testing: {url}")
    
    if has_redirect_pattern(url):
        print(f"🚨 Phishing Detected (Suspicious Redirect): {url}\n")
    
    elif is_suspicious_url(url):
        print(f"⚠️ Phishing Detected (Pattern Match): {url}\n")
    
    elif check_google_safe_browsing(url):
        print(f"🚨 Phishing Detected (Google Blacklist): {url}\n")
    
    else:
        print(f"✅ Safe URL: {url}\n")

print("✅ All tests completed.")

