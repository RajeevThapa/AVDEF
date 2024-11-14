import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_notification():
    # Get the workspace directory from the environment variable, default to current directory if not found
    workspace_dir = os.getenv('WORKSPACE', '.')

    # Path to the summary report (dynamically constructed based on the workspace)
    report_path = os.path.join(workspace_dir, "scans", "reports", "summary_report.md")

    # Check if the report exists
    if not os.path.exists(report_path):
        print(f"Error: Report file '{report_path}' not found.")
        return

    # Read the report content
    with open(report_path, "r") as report_file:
        report_content = report_file.read()

    # Compose email
    msg = MIMEMultipart()
    msg['Subject'] = 'Automated Vulnerability Scan Report'
    msg['From'] = os.getenv('SMTP_FROM', 'scanner@example.com')  # From address via environment variable
    msg['To'] = os.getenv('SMTP_TO', 'team@example.com')  # To address via environment variable

    # Email Body (Plain Text)
    msg.attach(MIMEText(report_content, 'plain'))

    # SMTP configuration using environment variables for security
    smtp_server = os.getenv('SMTP_SERVER', 'sandbox.smtp.mailtrap.io')
    smtp_port = int(os.getenv('SMTP_PORT', 587))  # Default to 587 if not set (for TLS)
    smtp_user = os.getenv('SMTP_USER', '2cb76ee748bacb')  # Mailtrap username
    smtp_password = os.getenv('SMTP_PASSWORD', 'ed891a165fdcef')  # Mailtrap password

    try:
        # Connect to SMTP server with TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        print("Notification sent successfully.")

    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_notification()

# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# def send_notification():
#     # Get the workspace directory from the environment variable, default to current directory if not found
#     workspace_dir = os.getenv('WORKSPACE', '.')

#     # Path to the summary report (dynamically constructed based on the workspace)
#     report_path = os.path.join(workspace_dir, "scans", "reports", "summary_report.md")

#     # Check if the report exists
#     if not os.path.exists(report_path):
#         print(f"Error: Report file '{report_path}' not found.")
#         return

#     # Read the report content
#     with open(report_path, "r") as report_file:
#         report_content = report_file.read()

#     # Compose email
#     msg = MIMEMultipart()
#     msg['Subject'] = 'Automated Vulnerability Scan Report'
#     msg['From'] = os.getenv('SMTP_FROM', 'scanner@example.com')  # From address via environment variable
#     msg['To'] = os.getenv('SMTP_TO', 'team@example.com')  # To address via environment variable

#     # Email Body (Plain Text)
#     msg.attach(MIMEText(report_content, 'plain'))

#     # SMTP configuration using environment variables for security
#     smtp_server = os.getenv('SMTP_SERVER', 'smtp.example.com')
#     smtp_port = int(os.getenv('SMTP_PORT', 587))  # Default to 587 if not set (for TLS)
#     smtp_user = os.getenv('SMTP_USER', 'scanner@example.com')
#     smtp_password = os.getenv('SMTP_PASSWORD', 'password')

#     try:
#         # Connect to SMTP server with TLS
#         with smtplib.SMTP(smtp_server, smtp_port) as server:
#             server.starttls()  # Start TLS encryption
#             server.login(smtp_user, smtp_password)
#             server.send_message(msg)

#         print("Notification sent successfully.")

#     except Exception as e:
#         print(f"Error sending email: {e}")

# if __name__ == "__main__":
#     send_notification()

# # import smtplib
# # import os
# # from email.mime.text import MIMEText
# # from email.mime.multipart import MIMEMultipart

# # def send_notification():
# #     # Path to the summary report
# #     report_path = "/home/rajeev/User_rajeev/AAU/AVDEF/scans/reports/summary_report.md"

# #     # Check if the report exists
# #     if not os.path.exists(report_path):
# #         print(f"Error: Report file '{report_path}' not found.")
# #         return

# #     # Read the report content
# #     with open(report_path, "r") as report_file:
# #         report_content = report_file.read()

# #     # Compose email
# #     msg = MIMEMultipart()
# #     msg['Subject'] = 'Automated Vulnerability Scan Report'
# #     msg['From'] = 'scanner@example.com'
# #     msg['To'] = 'team@example.com'

# #     # Email Body (Plain Text)
# #     msg.attach(MIMEText(report_content, 'plain'))

# #     # SMTP configuration
# #     smtp_server = 'smtp.example.com'
# #     smtp_port = 587  # Use 465 for SSL, 587 for TLS
# #     smtp_user = os.getenv('SMTP_USER', 'scanner@example.com')  # Use environment variable for username
# #     smtp_password = os.getenv('SMTP_PASSWORD', 'password')  # Use environment variable for password

# #     try:
# #         # Connect to SMTP server with TLS
# #         with smtplib.SMTP(smtp_server, smtp_port) as server:
# #             server.starttls()  # Start TLS encryption
# #             server.login(smtp_user, smtp_password)
# #             server.send_message(msg)

# #         print("Notification sent successfully.")

# #     except Exception as e:
# #         print(f"Error sending email: {e}")

# # if __name__ == "__main__":
# #     send_notification()
