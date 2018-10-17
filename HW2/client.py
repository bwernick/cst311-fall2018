#Bradley
#Alex
#TCP Client

from socket import *
import random

#server variables
serverName = 'localhost'
serverPort = 12000

#setup connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#name for the client
name = input('Input client name: ')
#random client number
num = random.randint(0,99)
#messgae to send to server
clientMsg = "Client " + num + ": " + name

#send message to server
clientSocket.send(clientMsg.encode())

#recieve message from server
serverMsg = clientSocket.recv(1024)

#Print recieved message
print (serverMsg.decode())

#close the socket
clientSocket.close()


