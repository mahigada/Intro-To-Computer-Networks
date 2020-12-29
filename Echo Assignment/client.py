#Name: Mahi Gada

#! /usr/bin/env python3
# Echo Client
import sys
import socket

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
count = int(sys.argv[3])
data = 'X' * count # Initialize data to be sent


# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)



# Send data to server
print("Sending data to   " + host + ", " + str(port) + ": " + data + " (" + str(count) + " characters)")
for i in range(3):
    try:
        clientsocket.sendto(data.encode(),(host, port))
        dataEcho, address = clientsocket.recvfrom(count)
        print("Receive data from " + address[0] + ", " + str(address[1]) + ": " + dataEcho.decode())
        break
    except:
        print("Message timed out")
        
# Receive the server response


#Close the client socket
clientsocket.close()
