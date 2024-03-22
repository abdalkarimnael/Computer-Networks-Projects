# 1200015, 1200275, 1200779
#UDP CLIENT
import socket
import time
# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Declare host name and its port
HOST_NAME='localhost'
HOST_PORT=5566
# Record the start time
start_time = time.time()
# Send the numbers from 0 to 1,000,000 to the server
for i in range(1000000):
    client_socket.sendto(str(i).encode(), (HOST_NAME, HOST_PORT))

# Record the end time
end_time = time.time()
# Send the "end of transmission" message to the server
client_socket.sendto(b'END', (HOST_NAME, HOST_PORT))
# Print the time required to send the packets
print(f'Time required to send the messages: {end_time - start_time:.4f} seconds')
# Close the socket
client_socket.close()
