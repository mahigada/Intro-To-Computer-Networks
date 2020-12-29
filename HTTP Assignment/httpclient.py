
#! /usr/bin/env python3
#Name: Mahi Gada
# HTTP Client
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
# Get the server hostname, port as command line arguments
args = sys.argv[1]
host=args.split(":")[0]
port=(args.split(":")[1]).split("/")[0]
port=int(port)
fileName=args.split("/")[1]
input = (host, port)

# Create UDP client socket. Note the use of SOCK_DGRAM
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientsocket.settimeout(1)
clientSocket.connect((host, port))
cached=False
cacheFile="cache.txt"
if(path.exists(cacheFile)):
    if(not path.exists(fileName)):
        cached=False
    else:
        cached=True
def makeCache (cacheFile):
    f = open(cacheFile, "w")
    log = codecs.open(fileName, "r", "utf-8")
    for line in log:
        f.write(line)
if(cached):
    secs = os.path.getmtime(fileName)
    t = time.gmtime(secs)
    last_mod_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
    data = 'GET /' + fileName + ' HTTP/1.1\r\nHost:'+ host + ':' + str(port) +'\r\nIf-Modified-Since: ' + last_mod_time + '\r\n\r\n'
    print("HTTP Request: \n" + data)
    clientSocket.send(data.encode())
    dataEcho = clientSocket.recv(1024)
    dataEcho=dataEcho.decode()
    if('200 OK' in dataEcho):
        makeCache(cacheFile)
    if ('304 Not Modified' not in dataEcho):
        print("\nFile has been modified\n")
    print("HTTP Response: \n" + dataEcho)
    

if(not cached):
    data = 'GET /' + fileName + ' HTTP/1.1\r\nHost:'+ host + ':' + str(port) + '\r\n\r\n'
    print("HTTP Request: \n" + data)
    clientSocket.send(data.encode())
    dataEcho = clientSocket.recv(1024)
    dataEcho=dataEcho.decode()
    print("HTTP Response: \n" + dataEcho)
    if('404 Not Found' not in dataEcho):
        makeCache(cacheFile)
    else:
        if(path.exists(cacheFile)):
            os.remove(cacheFile)
#Close the client socket
clientSocket.close()