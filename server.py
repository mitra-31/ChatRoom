import socket
import sys
import time

s = socket.socket() #Created a socket object
host = input("Enter host name >> ")  #To get a host name
port = 1234

try:
    s.connect((host,port))
    print("Connected to Server")
except:
    print("Connection Falied try later")

while True:
    client_message = s.recv(1024)
    client_message = client_message.decode()
    print("client >> ",client_message)
    message = input("You >> ")
    message = message.encode() #encoding messages
    s.send(message)