import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification():
    # Get workspace and report paths
    workspace_dir = os.getenv('WORKSPACE', '.')
    report_path = os.path.join(workspace_dir, "scans", "reports", "summary_report.md")

    # Check if the summary report exists
    if not os.path.exists(report_path):
        print(f"Error: Report file '{report_path}' not found.")
        return

    # Read the report content
    with open(report_path, "r") as report_file:
        report_content = report_file.read()

    # Compose the email
    msg = MIMEMultipart()
    msg['Subject'] = 'Automated Vulnerability Scan Report'
    msg['From'] = os.getenv('SMTP_FROM', 'scanner@example.com')
    msg['To'] = os.getenv('SMTP_TO', 'team@example.com')
    msg.attach(MIMEText(report_content, 'plain'))

    # SMTP server configuration from environment variables
    smtp_server = os.getenv('SMTP_SERVER', 'smtp.example.com')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_user = os.getenv('SMTP_USER', 'scanner@example.com')
    smtp_password = os.getenv('SMTP_PASSWORD', 'password')

    # Send the email using SMTP
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        print("Notification sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_notification()
