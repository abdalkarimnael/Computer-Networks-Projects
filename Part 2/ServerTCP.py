# 1200015, 1200275, 1200779
#TCP SERVER
import socket
import time

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Declare host name and its port
HOST_NAME='localhost'
HOST_PORT=5566
# Bind the socket to a local address and port
server_socket.bind((HOST_NAME, HOST_PORT))

# Start listening for incoming connections
server_socket.listen(1)

# Accept an incoming connection
client_socket, client_address = server_socket.accept()

# Initialize a counter for the number of messages received
count = 0
# Start the timer
start_time = time.time()
# Continuously receive messages from the client and count them
while True:
    # Receive up to 6 bytes of data from the client
    data = client_socket.recv(6)
    #print(data)
    #print('\n')
    # If no data was received, the connection was closed
    if not data:
        break

    # Increment the counter for the number of messages received
    count += 1
# Stop the timer
end_time = time.time()
# Close the client and server sockets
client_socket.close()
server_socket.close()

# Print the final count of messages received
print(f'Received {count} messages.')
# Print the time required to receive the packets
print(f'Time required to receive the messages: {end_time - start_time} seconds')