import socket


HOST = 'localhost' 

PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen(1)

print("Listening111")

c, addr = server_socket.accept()

print("Connected to " + str(addr))
 
while True:
	msg = c.recv(1024).decode()
	if not msg:
		break
	print("From Client: " + str(msg))
	msg2 = input() 
	c.send(msg2.encode('utf-8'))
#print ("Received " + msg.decode('utf-8'))
c.close()
