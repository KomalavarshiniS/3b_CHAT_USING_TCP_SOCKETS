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
