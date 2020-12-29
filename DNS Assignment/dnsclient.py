
#! /usr/bin/env python3
#Name: Mahi Gada
# DNS Client
import sys
import socket
import time
import struct
import random
# Get the server hostname, port as command line arguments
address = sys.argv[1]
port = int(sys.argv[2])
host = sys.argv[3]
input = (host, port)
# Create UDP client socket. Note the use of SOCK_DGRAM
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(1)
messageID = random.randint(0,100)
answerLength=0
returnCode=0
question=host + " A IN"
questionByte=question.encode()
questionLength=len(str(question))
print("Sending Request to  " + host + ", " + str(port) + ":")
print("Message ID: " + str(messageID))
print("Question Length: " + str(questionLength) + " bytes")
print("Answer Length: " + str(answerLength) + " bytes")
print("Question: " + str(question))
network=("!hhihh" + str(questionLength)+"s")
data = struct.pack("!hhihh" + str(questionLength)+"s", 1, returnCode, messageID, questionLength, answerLength, questionByte)
for i in range(3):
    try:
        clientsocket.sendto(data,(address, port))
        dataEcho, address = clientsocket.recvfrom(1024)
        serverInfo = struct.unpack('!hhihh', dataEcho[:12])
        questionLength=serverInfo[3]
        answerLength=serverInfo[4]
        messageID=serverInfo[2]
        returnCode=serverInfo[1]
        if(returnCode==0):
            network=("!hhihh" + str(questionLength)+"s" + str(answerLength)+"s")
            answerInfo = struct.unpack(network, dataEcho)
            question=answerInfo[5].decode()
            answer=answerInfo[6].decode()
            print("Received Response from  " + host + ", " + str(port) + ":")
            print("Return Code: 0 (No errors)")
            print("Message ID: " + str(messageID))
            print("Question Length: " + str(questionLength) + " bytes")
            print("Answer Length: " + str(answerLength) + " bytes")
            print("Question: " + str(question))
            print("Answer: " + str(answer))
        else:
            network= network=("!hhihh" + str(questionLength)+"s")
            answerInfo = struct.unpack(network, dataEcho)
            question=answerInfo[5].decode()
            print("Received Response from  " + host + ", " + str(port) + ":")
            print("Return Code: 1 (Name does not exist)")
            print("Message ID: " + str(messageID))
            print("Question Length: " + str(questionLength) + " bytes")
            print("Answer Length: " + str(answerLength) + " bytes")
            print("Question: " + str(question))
        break    
    except socket.timeout:
        if(i==2):
            print("Request timed out … Exiting Program.")
        else:
            print("Request timed out...")
#Close the client socket
clientsocket.close()