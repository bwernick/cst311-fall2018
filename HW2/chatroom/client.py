#Bradley
#Alex
#TCP Client

import socket
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(('localhost', 12000))

while True:

    # maintains a list of possible input streams
    sockets = [sys.stdin, server]

    read_sockets, wrSocket, erSocket = select.select(sockets, [], []) #getting the sockets with select

    for s in read_sockets:
        if s == server: # if connection from server socket
            message = s.recv(2048) # recieve its message
            print message #print the message
        else:
            message = sys.stdin.readline() # errors out if using input/raw_input
            server.send(message) # send message
            sys.stdout.write("<You>") # print seems to hate message
            sys.stdout.write(message) # so stdout is used instead
            sys.stdout.flush() #flush stdout
server.close()
