#! /usr/bin/env python3
#Name: Mahi Gada
# Ping Server
import sys
import socket
import random
import struct
# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

# Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
print("The server is ready to receive on port:  " + str(serverPort) + "\n")
# loop forever listening for incoming UDP messages
while True:
        rand = random.randint(0,10)
    #Receive and print the client data from "data" socket
        data, address = serverSocket.recvfrom(1024)
        seqNum = struct.unpack('!ii', data)[1]
        data = struct.pack('!ii', 2, seqNum)
        if rand<4:
            print("Message with sequence number " + str(seqNum +1) + " dropped")
            continue
    # Echo back to client
        serverSocket.sendto(data,address)
        print("Responding to ping request with sequence number " + str(seqNum+1))
