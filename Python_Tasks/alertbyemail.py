#!/usr/bin/env python3

### This script to Schedule a cron job for disk usage alert via Python email


import shutil
import smtplib
from email.mime.text import MIMEText

# -----------------------------
# Configuration
# -----------------------------
THRESHOLD = 80                     # Alert when disk usage > 80%
CHECK_PATH = "/"                  # Check root filesystem
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "yourmail@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "admin@example.com"

# -----------------------------
# Check disk usage
# -----------------------------
total, used, free = shutil.disk_usage(CHECK_PATH)

used_percent = (used / total) * 100

# -----------------------------
# Send alert email function
# -----------------------------
def send_email_alert(usage):
    subject = "Disk Usage Alert"
    
    body = f"""
Warning!

Disk usage on server has crossed threshold.

Current Usage: {usage:.2f}%
Threshold: {THRESHOLD}%

Please clean up disk space.
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    server.quit()

    print("Alert email sent successfully.")

# -----------------------------
# Main Logic
# -----------------------------
if used_percent > THRESHOLD:
    send_email_alert(used_percent)
else:
    print(f"Disk usage is normal: {used_percent:.2f}%")
