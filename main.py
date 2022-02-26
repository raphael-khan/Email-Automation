import smtplib
from email.message import EmailMessage, Message
from string import Template
from pathlib import Path # similar to os.path. Allows us to access index.html 

html = Template(Path('index.html').read_text()) # assigning file path, reading and wrapping it in an Template object so $name variable can be used. 
email = EmailMessage()
email['from'] = 'Raphael'
email['to'] = 'ralphfit101@gmail.com'
email['subject'] = ' New Developer to the team ! '

email.set_content(html.substitute({'name':'Raphael', 'date' : '05/01/2022'}) , 'html') # string or takes variable from the HTML and subs. Have to give the HTML parameter so it parases the file correctly.  

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # identify yourself to the server. 
    smtp.starttls() # starts an encrypted connection _ Transport Layer Security
    smtp.login('ralphfit101@gmail.com' , 'AccessGmail12!')
    smtp.send_message(email)
    print("your message was sent successfully !")