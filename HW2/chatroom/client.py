#Bradley
#Alex
#TCP Client

import socket
import sys
import select
import os


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(('localhost', 12000))

all_messages = [] # stores all messages from client and server

# prints all messages sent and recieved, in order
def showMessages():
    os.system('clear')  # 'clear' for linux/OS X, 'cls' for windows
    for msg in all_messages:
        sys.stdout.write(msg)


while True:

    # maintains a list of possible input streams
    sockets = [sys.stdin, server]

    read_sockets, wrSocket, erSocket = select.select(sockets, [], []) # getting the sockets with select

    for s in read_sockets:
        if s == server: # if connection from server socket
            message = s.recv(2048) # recieve its message
            all_messages.append(message)
            showMessages()
            if "Disconnected!" in message:
                if "> Disconnected!" in message:
                    continue
                else:
                    break

        else:
            message = sys.stdin.readline() # errors out if using input/raw_input
            server.send(message) # send message
            temp = "<You>" + message
            all_messages.append(temp) #add user message to the array of messages total
            showMessages()
            sys.stdout.flush() #flush stdout
    else:
        continue
    break
server.close()
