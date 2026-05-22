import socket

client = socket.socket()

client.connect(("localhost", 5000))

client.send("Hello Server".encode())

response = client.recv(1024).decode()

print("Server Response:", response)

client.close()
