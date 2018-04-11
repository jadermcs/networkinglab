from datetime import datetime
import smtpd
import asyncore
import os

box = "emailbox"

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print('Receiving message from:', peer)
        print('Message addressed from:', mailfrom)
        print('Message addressed to  :', rcpttos)
        print('Message length        :', len(data))
        filename = "{}.eml".format(datetime.now().strftime('%Y%m%d%H%M%S'))
        for rcp in rcpttos:
            ruser = box + '/' + rcp.split("@")[0]
            os.makedirs(ruser, exist_ok=True)
            with open(ruser + '/' + filename, 'w') as fout:
                fout.write(data)


server = CustomSMTPServer(('127.0.0.1', 1025), None)

asyncore.loop()
