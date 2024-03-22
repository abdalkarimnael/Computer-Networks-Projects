# 1200015, 1200275, 1200779
#TCP CLIENT
import socket
import time

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Declare host name and its port
HOST_NAME='localhost'
HOST_PORT=5566
# Connect to the server
server_address = (HOST_NAME, HOST_PORT)
sock.connect(server_address)

# Start the timer
start_time = time.time()

# Send the numbers from 0 to 1,000,000 to the server
for i in range(1000000):
    sock.sendall(str(i).encode())

# Stop the timer
end_time = time.time()

# Print the time required to send the packets
print(f'Time required to send the messages: {end_time - start_time} seconds')
# Close the connection
sock.close()
