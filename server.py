import socket
import time
import heapq

# Graph as adjacency list
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'D': 7},
    'C': {'A': 4, 'D': 1},
    'D': {'B': 7, 'C': 1, 'F': 3},
    'F': {'D': 3}
}

# Dijkstra function
def dijkstra(graph, start, end):
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return path, cost
        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (cost + graph[node][neighbor], neighbor, path + [neighbor]))
    return None, float('inf')

# Server code
server_socket = socket.socket()
server_socket.bind(('localhost', 8080))
server_socket.listen(1)
print("🚦 Control Center: Waiting for Emergency Vehicle connection...")

conn, addr = server_socket.accept()
print(f"✅ Connected with Emergency Vehicle at {addr}")

# Receive initial request
data = conn.recv(1024).decode()
print(f"[Server] Request received: {data}")

# Calculate initial route
route, dist = dijkstra(graph, 'A', 'F')
conn.send(f"Initial Route: {' → '.join(route)} (Distance: {dist})".encode())

# Simulate traffic congestion by increasing weight A→C
time.sleep(3)
print("⚠️ Traffic congestion detected on road C → D!")
graph['C']['D'] += 5
graph['D']['C'] += 5

# Recalculate route
route, dist = dijkstra(graph, 'A', 'F')
conn.send(f"Updated Route: {' → '.join(route)} (Distance: {dist})".encode())

conn.close()
server_socket.close()
