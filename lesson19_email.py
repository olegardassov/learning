#password dsf342asda
# python@mrartful.com
# smtp: smtp.zone.eu port 456 SSL/TLS or 587 STARTTLS

import smtplib
from email.message import EmailMessage


#STARTTLS
server = smtplib.SMTP('smtp.zone.eu', 587)
server.ehlo()
server.starttls()
server.ehlo()
#OR
#SSL
server = smtplib.SMTP_SSL('smtp.zone.eu', 465)
server.login('python@mrartful.com', 'dsf342asda')       # email you are sending from

msg = EmailMessage()
msg['Subject'] = 'Sample email sent by python'
msg['From'] = 'python@mrartful.com'
msg['To'] = 'olegardassov@gmail.com'

msg.set_content('Hello, this is my first email using Python.')  # will send this email, if your email does not support html
#OR
msg.add_alternative("""
    <!DOCTYPE>
    <html>
        <body>
            <h1 style="color: red;">Sample email</h1>
            <p>Hello this is sample email</p>
        </body>
    </html>
""", subtype='html')
server.send_message(msg)    # need to use name of variable, in our case msg
