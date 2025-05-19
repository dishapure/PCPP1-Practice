import socket

server = socket.socket()
server.bind(('localhost',12345))
server.listen(1)
print("SErver is running")

conn, addr = server.accept()
print("connect to", addr)

data = conn.recv(1024).decode()
print("recieved".data)

conn.send("hello from server".encode())
conn.close()