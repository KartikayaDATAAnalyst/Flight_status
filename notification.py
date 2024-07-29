import smtplib
from email.mime.text import MIMEText

def send_notification(flight_id, status, gate, delay):
    # Example: Sending an email notification
    msg = MIMEText(f'Flight {flight_id} status changed to {status}. Gate: {gate}, Delay: {delay}')
    msg['Subject'] = f'Flight {flight_id} Status Update'
    msg['From'] = 'noreply@flightstatus.com'
    msg['To'] = 'user@example.com'
    
    with smtplib.SMTP('smtp.example.com') as server:
        server.login('username', 'password')
        server.send_message(msg)
