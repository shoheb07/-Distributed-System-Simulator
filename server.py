import socket

server = socket.socket()

server.bind(("localhost", 5000))

server.listen(1)

print("Server Waiting for Connection...")

client, address = server.accept()

print("Connected to:", address)

message = client.recv(1024).decode()

print("Client Message:", message)

client.send("Message Received".encode())

client.close()
