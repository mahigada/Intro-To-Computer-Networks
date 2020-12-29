
#! /usr/bin/env python3
#Name: Mahi Gada
# Ping Client
import sys
import socket
import time
import struct
# Get the server hostname, port as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
rttArray = []
print ("Pinging " + host + ", " + str(port) + ":")
input = (host, port)
# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)
received =0
for i in range (0,10):
    time1 = time.time()
    data = struct.pack('!ii', 1,i)
    clientsocket.sendto(data, input)
    try:
        dataEcho, address = clientsocket.recvfrom(1024)
        time2=time.time()
        rtt=time2-time1
        rttArray.append(rtt)
        print ("Ping message number " + str(i + 1) + " RTT: " + str(rtt))
        received=received+1
    except:
        print("Ping message number " + str(i+1) + " timed out")
# Send data to server
i = i +1
print("Statistics: ")
packetLoss = (received/i)*100
average = sum(rttArray) / len(rttArray)
print(str(i) + " packets transmitted, " + str(received) + " received, " + str(packetLoss) + "% packet loss")
print("Min/Max/Av RTT = " + str(min(rttArray)) + " / "  + str(max(rttArray)) + " / " + str(average) + " secs")
    
#Close the client socket
clientsocket.close()
