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
