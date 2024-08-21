import smtplib
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def parse_build_output(build_output):
    test_summary = re.findall(r'(\d+) tests, (\d+) failures', build_output)
    if not test_summary:
        raise ValueError("No test summary found in build output.")
    total_tests, total_failures = test_summary[0]
    build_status = "SUCCESS" if int(total_failures) == 0 else "FAILURE"
    return {
        "total_tests": total_tests,
        "total_failures": total_failures,
        "build_status": build_status
    }
def send_email(summary, developer_emails):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "shourywardhan24@gmail.com"
    smtp_password = "bsod iqqx jrrr tqeq"
    from_email = smtp_username
    to_emails = developer_emails
    subject = f"Jenkins Build Summary: {summary['build_status']}"
    body = f"""
    Hello Team,
    Here is the summary of the latest Jenkins build:
    Total Tests: {summary['total_tests']}
    Total Failures: {summary['total_failures']}
    Build Status: {summary['build_status']}
    Best Regards,
    Jenkins Automation
    """
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_emails, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
if __name__ == "__main__":
    build_output = """
    zz
    """
    developer_emails = [
        "prathambaliyan012@gmail.com",
        "prathamlal0426@gmail.com"
    ]
    summary = parse_build_output(build_output)
    send_email(summary, developer_emails)
