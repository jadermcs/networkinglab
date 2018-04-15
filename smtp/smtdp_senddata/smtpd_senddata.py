import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'),
                                   ('Joao',
                                    'joaoud@example.com'))
msg['From'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('172.17.0.2', 1025)
server.set_debuglevel(True)  # show communication with the server
try:
    server.sendmail('author@example.com',
                    ['recipient@example.com', 'joaoud@example.com'],
                    msg.as_string())
finally:
    server.quit()
