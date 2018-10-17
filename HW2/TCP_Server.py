#Bradley
#Alex
#TCP Server

#TCPCapitalizationServer.py
from socket import *
serverPort = 12000

# Create a TCP socket
serverSocket = socket(AF_INET,SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind(('',serverPort))

#server is listening for packets
serverSocket.listen(1)
print ('The server is ready to receive')

while True:
    #connectionSocket, addr = serverSocket.accept()
    #sentence = connectionSocket.recv(1024).decode()

    #Strip the word client from recieved message

    #Wait for the second client to send a message

    #Determine which came first

    #Create message to send to both clients

    #send to both clients

    #connectionSocket.send(sentance.encode())
    #connectionSocket.close()