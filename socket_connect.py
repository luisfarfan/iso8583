import socket
import sys
import time

serverIP = "190.223.68.57"
serverPort = 10301
numberEcho = 5
timeBetweenEcho = 5  # in seconds

bigEndian = True


def send_to_socket(data):
    s = None
    for res in socket.getaddrinfo(serverIP, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except (socket.error):
            s = None
            continue
        try:
            s.connect(sa)
        except (socket.error):
            s.close()
            s = None
            continue
        break
    if s is None:
        print('Could not connect :(')
        sys.exit(1)

    for req in range(0, numberEcho):
        if bigEndian:
            try:
                print("Enviando: %s" % data)
                s.send(data)
                ans = s.recv(2048)
                print("\nRespuesta del socket %s" % ans)
                s.close()
                return ans
            except Exception as msg:
                print(msg)
                break

            time.sleep(timeBetweenEcho)

    print('Closing...')
    s.close()
