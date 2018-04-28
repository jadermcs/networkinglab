import smtplib
import email.utils
from email.mime.text import MIMEText
import socket
import sys

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Alice',
                                    'alice@mail.intranet'))
msg['From'] = email.utils.formataddr(('Bob',
                                      'bob@mail.intranet'))

msg['Subject'] = 'Simple test message'
server = smtplib.SMTP('mail.intranet', 25)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('bob@mail.intranet',
                    ['alice@mail.intranet'],
                    msg.as_string())
finally:
    server.quit()
