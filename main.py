import smtplib
from email.message import EmailMessage, Message

email = EmailMessage()
email['from'] = 'Raphael'
email['to'] = 'ralphfit101@gmail.com'
email['subject'] = 'Hi ! How are ya ?'

email.set_content(' This is my second message to you.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ralphfit101@gmail.com' , 'AccessGmail12!')
    smtp.send_message(email)
    print("your message was sent successfully !")