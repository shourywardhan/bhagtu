import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_error_email(stage_name, error_log, recipient_email):
    sender_email = "shourywardhan24@gmail.com"
    sender_password = "ozfsvokg qgbn  esqk"
    
    subject = f"Jenkins Pipeline Error in Stage: {stage_name}"
    body = f"""
    An error occurred in the Jenkins pipeline during the stage: {stage_name}.
    
    Error Log:
    {error_log}

    Please check the Jenkins console output for more details.
    """
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Send the email
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Error email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

if __name__ == "__main__":
    # These environment variables will be set by Jenkins
    stage_name = os.getenv('STAGE_NAME', 'Unknown Stage')
    build_status = os.getenv('BUILD_STATUS', 'UNKNOWN')
    error_log = os.getenv('ERROR_LOG', 'No error log available')
    recipient_email = os.getenv('DEVELOPER_EMAIL', 'developer@example.com')
    
    if build_status == "FAILURE":
        send_error_email(stage_name, error_log, recipient_email)
