from socket import *
import threading

# my server set up where the socket is created and it binds to a selected port
serSocket = socket(AF_INET, SOCK_STREAM)
serSocket.bind(('localhost', 0))  # This uses port 0 to pick a available port
serIP, serPort = serSocket.getsockname()
serSocket.listen(5)  # this looks for incoming connections which is up to 5

# prints the IP and Port number
print(f'Server IP is {serIP} on port {serPort}\n')

# allows for individual client connection to occur in separate threads
def handleClient(connSocket, addr):
    # Gives client details and creates new thread
    print(f'New thread for connection at port: {addr[1]}')
    print(f'Client IP address: {addr[0]}\n')

    try:
        # gets the clients HTTP request
        message = connSocket.recv(1024).decode()
        print(f'HTTP request received:\n{message}\n')

        # will parse the filename from HTTP request
        parts = message.split()
        if len(parts) > 1:
            filename = parts[1].lstrip('/')  # will remove all / from filename
        else:
            # will handle all malformed and empty request by shutting connection down
            connSocket.close()
            print('Empty or malformed request. Thread terminating.\n')
            return

        # will try opening and readinf the file
        with open(filename, 'rb') as file:
            outputdata = file.read()
            # prints contents
            print(f'File contents:\n{outputdata.decode()}\n')

            # sends message to HTTP(200 OK)
            header = 'HTTP/1.1 200 OK\r\n\r\n'
            print(header.strip())  # prints 200 OK in terminal
            connSocket.send(header.encode())

            # sends the file content
            connSocket.send(outputdata)

    except FileNotFoundError:
        # creates file error so sends 404 Not Found
        print('Error: File not found\n')
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connSocket.send(header.encode())
        # HTML content 404 message
        connSocket.send(b'<html><body><h1>404 Not Found</h1></body></html>')

    finally:
        # terminate thread and close client connection
        connSocket.close()
        print('Thread terminating\n')

# main server loop which accepts connection continuously
try:
    while True:
        # accepts all new client connection
        connSocket, addr = serSocket.accept()
        print('New client connected')

        # creates / start new thread for client 
        client_thread = threading.Thread(target=handleClient, args=(connSocket, addr))
        client_thread.start()

# allows for easy shutdown or server(Ctrl+C)
except KeyboardInterrupt:
    print('\nServer is shutting down...')
finally:
    # close the server socket
    serSocket.close()
    print('Server socket closed')
