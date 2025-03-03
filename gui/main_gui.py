import customtkinter as ctk
from tkinter import messagebox
from modules.api_checker import check_google_safe_browsing
from modules.url_checker import is_suspicious_url, has_redirect_pattern

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

