import socket

HOST = 'localhost'

PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    sock.connect((HOST, PORT))

except Exception as e:

    print("Cannot connect to the server:", e)

print("Connected")

message = input()
#sock.send("hello".encode('utf-8'))
while message.lower().strip() != 'done':
	sock.send(message.encode('utf-8'))
	message2 = sock.recv(1024).decode('utf-8')
	print("From Server: " + str(message2))
	message = input()

sock.close()
