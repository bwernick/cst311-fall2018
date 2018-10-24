# Bradley
# Alex
# TCP Server

# TCP Server.py
import socket
import thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('localhost',12000))

server.listen(100)
clients = []

print("Waiting for connections...")

def clientThread(conn, addr):
    # Connection message
    conn.send("Connected!")
    # loop forever to handle any messages from client
    while True:
        try:
            message = conn.recv(2048)
            if message:
                print "<" + addr[0] + "> " + message

                # Send message to all
                sendMsg = "<" + addr[0] + "> " + message
                broadcast(sendMsg, conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()
                # remove the client
                remove(client)

def remove(connection):
    if connection in clients:
        clients.remove(connection)


while True:
    conn, addr = server.accept()
    clients.append(conn)

    # prints the address of the user that just connected
    print addr[0] + " connected."

    # creates and individual thread for every user
    # that connects
    thread.start_new_thread(clientThread, (conn, addr))

conn.close()
server.close()
