# Bradley
# Alex
# TCP Server

# TCPCapitalizationServer.py
from socket import *
import thread

client_list = []
serverPort = 12000          # reserving a port

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind(('', serverPort))

# server is listening for packets
serverSocket.listen(100)

print ('The server is ready to receive')
print ('Waiting for clients...')

# sending messages
def broadcast(msg, conn):
    for client in client_list:
        # if not the sending client
        if client != conn:
            try:
                # send the message to other clients
                client.send(msg)
            except:
                # no connection clients get removed
                client.close()
                remove(client)

# removing specific clients
def remove(conn):
    if conn in client_list:
        client_list.remove(conn)


def on_new_client(clientsocket,addr):
    while True:
        # get message
        msg = clientsocket.recv(1024)
        # print message server side
        print "<", addr, ">", ': ', msg
        # generate messsage to send
        sendMsg = "<" + addr + ">" + ': ' + msg
        # send to all other clients
        broadcast(sendMsg, clientsocket)
    clientsocket.close()

while True:
    # get connection from client
    c, addr = serverSocket.accept()
    # add new client to list of clients
    client_list.append(c)
    # connected message
    print addr, " connected."
    # new thread for each new client
    thread.start_new_thread(on_new_client(c,addr))

serverSocket.close()