import socket
# import multiprocessing
# start keeping notes


def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    # make listening a differnt thread
    # when connection made from client quit listening
    # when makeing connection quit to another server
    # become client quit listening
    s.listen(3)
    # while True:
    #    p = multiprocessing.Process(target=thread
    print('here we go')
    c, addr = s.accept()
    print ('what is this ' + str(c))
    print ('Connection from: ' + str(addr))
    while True:
        incoming = c.recv(1024)
        data = incoming.decode('utf-8')
        print ('just decoded')
        if not data:
            print ('break happening')
            break
        print ('from connected user: ' + str(data))
        data = str(data).upper()
        print ("sending: " + str(data))
        c.send(data.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    Main()
