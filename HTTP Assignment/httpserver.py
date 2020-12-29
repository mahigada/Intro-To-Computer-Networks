#! /usr/bin/env python3
#Name: Mahi Gada
# HTTP Server
import sys
import socket
import time
import struct
import random
import datetime
import time
import codecs
import os.path
from os import path

# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
dataLen = 1000000
# Create a TCP "welcoming" socket. Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
# Listen for incoming connection requests
serverSocket.listen(1)
print('The server is ready to receive on port:  ' + str(serverPort) + '\n')
# loop forever listening for incoming connection requests on "welcoming" socket
lst=[] * 2
def getReq (fileName):
    log = open(fileName, "r").read()
    content_length = len(log)
    secs = os.path.getmtime(fileName)
    t = time.gmtime(secs)
    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
    lst.insert(0, last_mod_time)
    data='HTTP/1.1 200 OK\r\n' + 'Date: ' + date + 'Last-Modified: ' + last_mod_time + 'Content-Length:' + str(content_length) + '\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n' + log
    connectionSocket.send(data.encode())

while True:
    # Accept incoming connection requests; allocate a new socket for data communication
    connectionSocket, address = serverSocket.accept()
    #print("Socket created for client " + address[0] + ", " + str(address[1]))
    # Receive and print the client data in bytes from "data" socket
    data = connectionSocket.recv(dataLen).decode()
 
    fileName = data.split("/")[1]
    fileName=fileName.split()[0]
    t = datetime.datetime.now()
    date = t.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n")
    
    if(path.exists(fileName)):
        if ('Modified' in data):
            compare = data.split("If-Modified-Since: ",1)[1]
            t = time.strptime(compare+'\r\n', "%a, %d %b %Y %H:%M:%S %Z\r\n")
            secs2 = time.mktime(t)
            last_mod_comp = lst[0]
            t1 = time.strptime(last_mod_comp, "%a, %d %b %Y %H:%M:%S %Z\r\n")
            secs1 = time.mktime(t1)
           
            if(secs2<=secs1):
                data='HTTP/1.1 304 Not Modified\r\nDate: ' + date +'\r\n\r\n'
          
                connectionSocket.send(data.encode())
            else:
                getReq(fileName)
        else:
            getReq(fileName)
    else:
        data='HTTP/1.1 404 Not Found\r\nDate: ' + date + 'Content-Length: 0\r\n\r\n'
        connectionSocket.send(data.encode())
