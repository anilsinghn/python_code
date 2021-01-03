# using this code you can send message without using your browser.
import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from']= 'anil singh'
email['to']= 'arun.sinngh@gmail.com'
email['subject']= 'you won 1M dollars!'

email.set_content('i am a scammer')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('blazegaming560@gmail.com','Myattitude@1')
    smtp.send_message(email)
    print("all good boss")
