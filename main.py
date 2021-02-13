import socket
import sys
import time

s = socket.socket() #Created a socket object
host = socket.gethostname()  #To get a host name

print("Host : ",host)

port = 1234 #Port Number 

s.bind((host,port)) 
print("Connected")

s.listen(1) 

conn,add = s.accept()

while True:
    message = input("You >> ")
    message = message.encode() #encoding messages
    conn.send(message)
    client_message = conn.recv(1024)
    client_message = client_message.decode()
    print("client >> ",client_message)