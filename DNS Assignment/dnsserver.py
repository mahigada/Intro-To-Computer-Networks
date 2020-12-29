#! /usr/bin/env python3
#Name: Mahi Gada
# DNS Server
import sys
import socket
import random
import struct
#Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

#Create a UDP socket. Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Assign server IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
#loop forever listening for incoming UDP messages
while True:
    lineList=[]
    file=open("dns-master.txt", "r").readlines()
    for line in file:
        lineList.append(line.strip())
    data, address = serverSocket.recvfrom(1024)
    data2 = struct.unpack('!hhihh', data[0:12])
    questionLength=data2[3]
    messageID=data2[2]
    network=("!hhihh" + str(questionLength)+"s")
    data3 = struct.unpack("!hhihh" + str(questionLength)+"s", data)
    question=data3[5].decode()
    returnCode=1
    questionByte=question.encode()
    x=False
    for answer in lineList:
        compare=answer.replace('3600 ', '')
        compare=compare.split('IN')[0]
        compare=compare+"IN"
        answerLength=len(str(answer))
        answerByte=answer.encode()
        if (compare==question):
            x=True
            break
    if(x):
        network=(network + str(answerLength)+"s")
        returnCode=0
        data = struct.pack(network, 2, returnCode, messageID, questionLength, answerLength, questionByte, answerByte)
        serverSocket.sendto(data,address)
    if(not x):
        data4 = struct.pack("!hhihh" + str(questionLength)+"s", 2, returnCode, messageID, questionLength, 0, questionByte)
        serverSocket.sendto(data4,address)