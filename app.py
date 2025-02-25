import re
import requests
import customtkinter as ctk
from tkinter import messagebox

GOOGLE_API_KEY = "your_google_api_key"  # Replace with your actual API Key

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
        r"https?:\/\/.*\b[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}\b",  # Check for email-like structure in URL (e.g., google.com-redirect@valimail.com)
    ]
    return any(re.search(pattern, url) for pattern in phishing_patterns)

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
    response = requests.post(api_url, json=payload)
    result = response.json()
    return "matches" in result  # If URL is found in the database, it's phishing

def has_redirect_pattern(url):
    """Check if the URL contains suspicious redirect patterns using @ symbol."""
    if "@" in url:
        if re.search(r".*-.*@.*", url):
            return True
    return False

def scan_url():
    """Scan the entered URL and display the result."""
    url = url_entry.get().strip()
    
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return
    
    result_label.configure(text="🔎 Scanning...", text_color="blue")
    root.update_idletasks()
    
    if has_redirect_pattern(url):
        result_label.configure(text="🚨 Phishing Detected (Suspicious Redirect/Email-like)", text_color="red")
    elif is_suspicious_url(url):
        result_label.configure(text="⚠️ Phishing Detected (Pattern Match)", text_color="orange")
    elif check_google_safe_browsing(url):
        result_label.configure(text="🚨 Phishing Detected (Google Blacklist)", text_color="red")
    else:
        result_label.configure(text="✅ Safe URL", text_color="green")

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

root = ctk.CTk()
root.title("Phishing Link Scanner")
root.geometry("450x350")
root.resizable(False, False)

title_label = ctk.CTkLabel(root, text="🔍 Phishing Link Scanner ~By hecker2610", font=("Arial", 18, "bold"))
title_label.pack(pady=15)

url_entry = ctk.CTkEntry(root, width=300, height=40, font=("Arial", 18), placeholder_text="Enter URL...")
url_entry.pack(pady=10)

scan_button = ctk.CTkButton(root, text="Scan", font=("Arial", 18), command=scan_url)
scan_button.pack(pady=10)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 16))
result_label.pack(pady=10)

root.mainloop()
