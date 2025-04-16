#import socket module 
from socket import * 
import sys  # In order to terminate the program 

serverSocket = socket(AF_INET, SOCK_STREAM) 

# Prepare a server socket 
serverPort = 6789  # This is the serverport number we are listinng in
serverSocket.bind(('', serverPort))  # I have a blind socket for the address/port
serverSocket.listen(1)  # This is listening for incoming connections

while True:
    # Establish the connection
    print('Ready to serve...')
    
    connectionSocket, addr = serverSocket.accept()  # Allowing for the incoming connection to connect

    try:
        #  Will receive the request message 
        message = connectionSocket.recv(1024).decode()  
        print("Request message:", message)  

        # Will ask for file from message
        filename = message.split()[1]  
        f = open(filename[1:])  

        # Will read file info
        outputdata = f.read()

        # This will send HTTP response header
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

        # This will send all the content we got to the file that has been requested
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # This is the message it will send if file not found in local server
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        connectionSocket.close()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
