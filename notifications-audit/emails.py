import smtplib
from email.message import EmailMessage
from logs.audit_logger import log_action

def send_email(to_email, subject, message):
    try:
        sender_email = "your_email@gmail.com"
        sender_password = "your_app_password"  # Use App Password

        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(message)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        log_action(f"Email sent to {to_email}")

    except Exception as e:
        log_action(f"Email failed: {e}")
