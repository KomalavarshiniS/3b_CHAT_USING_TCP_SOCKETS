# 3b.CREATION FOR CHAT USING TCP SOCKETS
## AIM:
To write a python program for creating Chat using TCP Sockets Links.
## ALGORITHM:
1. Import the necessary modules in python
2. Create a socket connection to using the socket module.
3. Send message to the client and receive the message from the client using the Socket module in
 server
4. Send and receive the message using the send function in socket.
## PROGRAM:
### Client.py
```
import socket
s = socket.socket()
s.connect(('localhost', 8000))
while True:
    msg = input("Client > ")
    s.send(msg.encode())
    data = s.recv(1024).decode()
    print("Server >", data)
    if msg.lower() == 'exit':
        print("Closing connection...")
        break
s.close()
```
### Server.py
```
import socket
s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print("Server is waiting for connection...")
c, addr = s.accept()
print("Connected to:", addr)
while True:
    client_message = c.recv(1024).decode()
    print("Client >", client_message)

    msg = input("Server > ")
    c.send(msg.encode())

    if msg.lower() == 'exit':
        print("Closing connection...")
        break

c.close()
s.close()
```
## OUPUT:
### Clinet.py
![alt text](<Screenshot 2025-10-28 024228.png>)
### Server.py
![alt text](<Screenshot 2025-10-28 024235.png>)
## RESULT:
Thus, the python program for creating Chat using TCP Sockets Links was successfully 
created and executed.
