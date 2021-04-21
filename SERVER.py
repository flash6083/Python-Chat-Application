import socket
import sys
import time

s = socket.socket()
host = input('Please enter the host you want to connect to: ')
port = 1025

try:
    s.connect((host,port))
    print('Connected to host')

except:
    print('Connection failed')

while True:

    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print('Reply received: ',incoming_message)

    message = input('Enter your message ')
    message = message.encode()
    s.send(message)