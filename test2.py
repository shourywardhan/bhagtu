import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
                
def send_error_email(stage_name, error_log, recipient_email, sender_email, smtp_password):  
  subject = f"Jenkins Pipeline Error in Stage: {stage_name}"
  body = f'''
            An error occurred in the Jenkins pipeline during the stage: {stage_name}.
            Error Log:
            {error_log}
            Please check the Jenkins console output for more details.
            '''
  msg = MIMEMultipart()
  msg['From'] = sender_email
  msg['To'] = recipient_email
  msg['Subject'] = subject
  msg.attach(MIMEText(body, 'plain'))            
                    
                    # Send the email
  try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, smtp_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
    print("Error report sent successfully")
  except Exception as e:
    print(f"Failed to send email: {e}")

if __name__ == "__main__":
  smtpUsername = "shourywardhan24@gmail.com"
  smtpPassword = "bsod iqqx jrrr tqeq"
  stage_name = os.getenv('STAGE_NAME', 'Unknown Stage')
  error_log = os.getenv('ERROR_LOG', 'No error log available')
  recipient_email = os.getenv('DEVELOPER_EMAIL', 'prathambaliyan012@gmail.com')            
    if os.getenv('BUILD_STATUS') == "FAILURE":
      send_error_email(stage_name, error_log, recipient_email, "${smtpUsername}", "${smtpPassword}")
                            
