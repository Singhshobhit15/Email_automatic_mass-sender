from dotenv import load_dotenv
import os
import smtplib
from smtplib import SMTPException

# Load environment variables from .env file
load_dotenv()

# Retrieve the environment variables
email_id = os.getenv('EMAIL_ADDRESS')
email_pass = os.getenv('EMAIL_PASS')

# Debugging: Print out the values to ensure they are loaded (Be cautious with sensitive information)
print(f"EMAIL_ADDRESS: {email_id}")
print(f"EMAIL_PASS: {'*' * len(email_pass) if email_pass else None}")

if email_id is None or email_pass is None:
    raise ValueError("Email credentials are not set in environment variables")

try:
    # Connect to the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    #     smtp.ehlo()  # Can be omitted; automatically sent by starttls()
    #     smtp.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    #     smtp.ehlo()  # Can be omitted; automatically sent by starttls()

        # Log in to the SMTP server
        smtp.login(email_id, email_pass)

        # Compose the email
        subject = 'Fight Against Coronavirus'
        body = "Hey, let's fight against coronavirus by staying at home"
        msg = f'Subject: {subject}\n\n{body}'

        # Send the email
        smtp.sendmail(email_id, 'kishan15bhiii@gmail.com', msg)
        print("Email sent successfully!")

except SMTPException as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
