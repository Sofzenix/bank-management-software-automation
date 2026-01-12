from logs.audit_logger import log_action
import datetime

def send_sms(phone_number, message):
    timestamp = datetime.datetime.now()
    
    # Simulated SMS (for college project)
    print(f"[SMS] {timestamp} | To: {phone_number} | Message: {message}")

    log_action(f"SMS sent to {phone_number}")
