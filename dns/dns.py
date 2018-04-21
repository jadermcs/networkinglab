from datetime import datetime
import smtpd
import asyncore
import os
import threading
import socket


ip_table = {
    'gmail.com': '172.17.0.2',
    'hotmail.com': '172.17.0.3',
    'http.com':'172.17.0.4'
}

ip = '127.0.0.1'
# ip = '172.17.0.4'
serverport = 1053
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((ip, serverport))
# serverSocket.listen(1)

while True:
    print('\nwaiting to receive message')
    data, address = serverSocket.recvfrom(4096)



    if data:
        d = data.decode('utf-8')
        try:
            i = ip_table[d.strip()]
            sent = serverSocket.sendto(i.encode(), address)
        except Exception:
            serverSocket.sendto('host nao existe'.encode(), address)
        
