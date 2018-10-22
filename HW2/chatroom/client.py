#Bradley
#Alex
#TCP Client

from socket import *
import sys
import select

#server variables
serverName = 'localhost'
serverPort = 12000

#setup connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# message sending/ receiving loop
while True:
    # input streams
    sockets = [sys.stdin,clientSocket]

    # select gives input for reading input
    socket_read = select.select(sockets)

    for sock in socket_read:
        # if server has a message
        if sock == clientSocket:
            msg = sock.recv(1024)
            # print the server message
            print msg
        else:
            # if user inputs
            msg = sys.stdin.readline()
            #send the user input to server
            clientSocket.send(msg)
            print("<You>")
            print(msg)

clientSocket.close()

