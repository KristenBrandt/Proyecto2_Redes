"""
Universidad del Valle de Guatemala
Seccion 10
Ing. Jorge Yass
client.py
Proposito: Juego de carta utilizando pygame.

"""
#todo
#ok
#Va entonces mira, hagamos primero otro progroama, siendo la libreria para cliente y server.

# Se llama utils.py
import select, socket, sys
from utils import *
import utils

READ_BUFFER = 8192

#host name is 5555
if len(sys.argv) < 2:
    print("Usage: Python3 client.py [hostname]", file = sys.stderr)
    sys.exit(1)
else:

    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_connection.connect((sys.argv[1], utils.PORT))


def prompt():
    print('-->', end=' ', flush = True)

print("Connected to server\n")
msg_prefix = ''

socket_list = [sys.stdin, server_connection]

while True:
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])
    for s in read_sockets:
        if s is server_connection: # incoming message
            message = s.recv(READ_BUFFER)
            if not message:
                print("Server down!")
                sys.exit(2)
            else:
                if message == utils.quitting:
                    sys.stdout.write('Bye\n')
                    sys.exit(2)
                else:
                    sys.stdout.write(message.decode())
                    if 'Please tell us your name' in message.decode():
                        msg_prefix = 'name: ' # identifier for name
                    else:
                        msg_prefix = ''
                    prompt()

        else:
            message = msg_prefix + sys.stdin.readline()
            server_connection.sendall(message.encode())
