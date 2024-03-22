# 1200015, 1200275, 1200779
#UDP SERVER
import socket
import time
# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Declare host name and its port
HOST_NAME='localhost'
HOST_PORT=5566
# Bind the socket to a local address and port
server_socket.bind((HOST_NAME, HOST_PORT))

# Initialize a counter for the number of messages received
count = 0
# Record the start time
start_time = time.time()
# Continuously receive messages from the client and count them
while True:
    # Receive up to 6 bytes of data from the client
    data, client_address = server_socket.recvfrom(6)
    #print(data)
    #print('\n')
    # If the message received is the special "end of transmission" message, exit the loop
    if data == b'END':
        break
    # Increment the counter for the number of messages received
    count += 1
# Record the end time
end_time = time.time()

# Close the server socket
server_socket.close()

# Print the final count of messages received
print(f'Received {count} messages.')
# Print the time required to receive the packets
print(f'Time required to receive the messages: {end_time - start_time:.4f} seconds')
