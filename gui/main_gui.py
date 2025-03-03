import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def check_phishing():
    url = url_entry.get().strip()

    if not url.startswith("http"):
        url = "http://" + url  # Ensure valid URL format

    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        warning_keywords = ["login", "password", "verify", "bank", "account"]
        text = soup.text.lower()

        if any(keyword in text for keyword in warning_keywords):
            result_label.config(text="⚠️ Warning: This may be a phishing site!", fg="red", bg="white")
        else:
            result_label.config(text="✅ This website seems safe.", fg="green", bg="white")

    except requests.exceptions.RequestException:
        result_label.config(text="❌ Could not access the website!", fg="black", bg="white")

# GUI Setup
root = tk.Tk()
root.title("Phishing Link Scanner")
root.geometry("400x250")
root.configure(bg="lightgray")

tk.Label(root, text="Enter URL:", font=("Arial", 12), bg="lightgray").pack(pady=10)
url_entry = tk.Entry(root, width=40)
url_entry.pack()

scan_button = tk.Button(root, text="Check URL", command=check_phishing, font=("Arial", 12))
scan_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgray", width=50, height=2)
result_label.pack(pady=10)

root.mainloop()

