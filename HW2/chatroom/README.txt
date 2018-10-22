TCP_Server.py:
The idea behind this was found through research on servers handling multiple clients.
That answer was making a thread for each new client.
Furthermore, the server sends any message recieved to all clients other than the initial sender.
Thus, the server should be able to handle more than two clients.

client.py:
The idea for the client is to loop forever, and to handle server input and user input.
If the server has input, print it to the screen.
If the user has input, send it to the server, and print it to the user screen as well.
This should give the impression of a proper chatroom.
