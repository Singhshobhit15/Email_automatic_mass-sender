import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from smtplib import SMTPException


load_dotenv()

# Directly set your email credentials
email_id = 'shobhit15feb2001@gmail.com'
email_pass = 'aheyiqqtsgjkxayd'  # Use an app password if 2-Step Verification is enabled

# Debugging: Print out the values to ensure they are set correctly
print(f"EMAIL_ADDRESS: {email_id}")
print(f"EMAIL_PASS: {email_pass}")

if not email_id or not email_pass:
    raise ValueError("Email credentials are not set")

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_id, email_pass)

        subject = 'Fight Against Coronavirus'
        body = "Hey, let's fight against coronavirus by staying at home"

        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject'] = subject
        msg['From'] = email_id
        msg['To'] = 'kishan15bhiii@gmail.com'  # Correct the recipient address

        smtp.send_message(msg)
        print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")
