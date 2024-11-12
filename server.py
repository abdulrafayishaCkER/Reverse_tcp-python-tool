#!/usr/bin/python3

import socket
import subprocess

# Create a socket object
# We create a socket object using the socket.socket() function, which returns a socket object.
# The arguments to the function are:
#   - socket.AF_INET: This specifies the address family, which is IPv4 in this case.
#   - socket.SOCK_STREAM: This specifies the socket type, which is a connection-oriented(TCP), reliable, stream-based socket.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket option to reuse the address
# We set the socket option to reuse the address using the setsockopt() function.
# This allows the server to reuse the same address and port number even if the previous connection was not closed properly.
# The arguments to the function are:
#   - socket.SOL_SOCKET: This specifies the level at which the option is defined.
#   - socket.SO_REUSEADDR: This specifies the option to reuse the address.
#   - 1: This enables the option.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Define the server's IP address and port number
server_ip = '0.0.0.0'  #listen for all the incoming connections
server_port = 8080

# Bind the socket to the server's IP address and port number
# We bind the socket to the server's IP address and port number using the bind() function.
# This associates the socket with a specific address and port number.
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
# We put the socket into listening mode using the listen() function.
# This allows the server to accept incoming connections.
# The argument to the function is the maximum number of pending connections.
server_socket.listen(1)

print("Server listening on {}:{}".format(server_ip, server_port))

# Accept incoming connections
# We accept an incoming connection using the accept() function.
# This returns a new socket object (client_socket) and the address of the client.
client_socket, client_address = server_socket.accept()

print("Connection established with client {}".format(client_address))

while True:
    # Receive commands from the server
    # We receive commands from the server using the input() function.
    # This is a simple way to get user input, but in a real-world scenario, you would want to handle errors and exceptions.
    command = input("$ ")

    # Send the command to the client
    # We send the command to the client using the send() function.
    client_socket.send(command.encode())

    if command == "exit":
        # Exit the client and server
        # If the command is "exit", we break out of the loop and close the sockets.
        break

    # Receive the output from the client
    # We receive the output from the client using the recv() function.
    # This returns a bytes object, which we decode to a string using the decode() function.
    output = (client_socket.recv(1024)).decode()

    # Print the output
    # We print the output to the console.
    print(output)

# Close the sockets
# We close the client socket and server socket using the close() function.
client_socket.close()
server_socket.close()
