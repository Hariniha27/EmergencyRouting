import socket

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Send request to server
request = "Emergency Vehicle - From: A  To: F"
print(f"[Client] Sending data: {request}")
client_socket.send(request.encode())

# Receive initial route
initial_route = client_socket.recv(1024).decode()
print(f"[Client] Received: {initial_route}")

# Wait for updated route from server
updated_route = client_socket.recv(1024).decode()
print(f"[Client] Received updated route: {updated_route}")

client_socket.close()
