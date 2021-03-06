import socket


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))
    message = "Connection Ready!"
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024)
        print ('Received from server: ' + (data.decode('utf-8')))
        message = input("--> ")
    s.close()

if __name__ == '__main__':
    Main()
