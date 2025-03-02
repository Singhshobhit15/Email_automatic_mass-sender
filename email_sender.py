from dotenv import load_dotenv
import os
import smtplib
from smtplib import SMTPException
import imghdr
from email.message import EmailMessage

load_dotenv()

# Retrieve the environment variables
email_id = os.getenv('EMAIL_ADDRESS')
email_pass = os.getenv('EMAIL_PASS')

print(f"EMAIL_ADDRESS: {email_id}")
print(f"EMAIL_PASS: {'*' * len(email_pass) if email_pass else None}")

contacts = ['example@gmail.com',]

msg = EmailMessage()
msg['subject']= 'testing for automation with images'
msg['from']= email_id
# msg['to']= 'asdfg@gmail.com'
msg['to']= ','.join(contacts)
msg.set_content("image has been attached.hey ,this message is for testing purpose.Dont get offended ")

files = ['ss resume 3.pdf']
for file in files:
  with open(file,'rb') as m:
    file_data = m.read()
    # file_type = imghdr.what(m.name)
    file_name = m.name
    # print(file_type)
  msg.add_attachment(file_data, maintype = 'image', subtype = 'octet-stream', filename = file_name)
# Debugging: Print out the values to ensure they are loaded (Be cautious with sensitive information)


if email_id is None or email_pass is None:
    raise ValueError("Email credentials are not set in environment variables")

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      
     smtp.login(email_id, email_pass)
     smtp.send_message(msg)

    print("Email sent successfully!")

except SMTPException as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
