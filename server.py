"""
Universidad del Valle de Guatemala
Seccion 10
Ing. Jorge Yass
server.py
Proposito: Juego de carta utilizando pygame.

"""
#ip KRISTEN 192.168.1.6
#TODO
import select, socket, sys
from utils import *
import utils
READ_BUFFER = 8192

host = sys.argv[1] if len(sys.argv) >= 2 else ""


listen_socket = utils.create_socket((host, utils.PORT))

gameServer = gameServer()
connection_list = []
connection_list.append(listen_socket)

while True:
    # Player.fileno()
    read_players, write_players, error_sockets = select.select(connection_list, [], [])
    for player in read_players:
        if player is listen_socket: #nueva conexion, y se crea un socket
            new_socket,add = player.accept()
            new_player = Player(new_socket, add[1])
            connection_list.append(new_player)
            gameServer.greet_new_players_in_server(new_player)

        else: #nuevos mensajes recibidos y se convierten en upper cases
            message = player.socket.recv(READ_BUFFER)
            if message:
                message = message.decode().upper()
                print(message)
                if "NAME" in message:
                    nnn = message.split()[1]
                    player.setName(nnn)
                elif "QUIT" in message:
                    player.socket.sendall(b"Saliendo del chat...")
                    connection_list.remove(player)
                    player.socket.close()
                    break
                gameServer.client_menu(player, message)

            else:
                player.socket.close()
                connection_list.remove(player)

    for sock in error_sockets:
        #en caso de error, se desactiva el socket establecido
        sock.close()
        connection_list.remove(sock)
