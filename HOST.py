import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("Your connection is starting on: ",host)
port = 1025

s.bind((host,port))
print('Server is ready to accept')

s.listen(1)
connection,addr = s.accept()
print('Connection established to address: ',addr)

while True:
    message = input('Enter your message ')
    message = message.encode()
    connection.send(message)

    incoming_message = connection.recv(1024)
    incoming_message = incoming_message.decode()
    print('Reply received: ',incoming_message)


