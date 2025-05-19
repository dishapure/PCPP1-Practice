import socket

client = socket.socket()
client.connect(('localhost', 12345))

client.send("Hi Server!".encode())
response = client.recv(1024).decode()

print("Server says:", response)
client.close()
