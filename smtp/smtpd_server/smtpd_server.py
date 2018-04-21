from datetime import datetime
import smtpd
import asyncore
import os
import threading
import socket
import pop3

box = "emailbox"



class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print('[DEBUG] Receiving message from:', peer)
        print('[DEBUG] Message addressed from:', mailfrom)
        print('[DEBUG] Message addressed to  :', rcpttos)
        print('[DEBUG] Message length        :', len(data))
        filename = "{}.eml".format(datetime.now().strftime('%Y%m%d%H%M%S'))
        for rcp in rcpttos:
            ruser = box + '/' + rcp.split("@")[0]
            os.makedirs(ruser, exist_ok=True)
            with open(ruser + '/' + filename, 'w') as fout:
                fout.write(data)




server = CustomSMTPServer(('172.17.0.2', 1025), None)
smtp_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
pop3_thread = threading.Thread(target=pop3.init,name="pop3loop")
# If you want to make the thread a daemon
# loop_thread.daemon = True

smtp_thread.start()
pop3_thread.start()