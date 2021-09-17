"""
Universidad del Valle de Guatemala
Seccion 10
Ing. Jorge Yass
utils.py
Proposito: Funciones y clases para client y server
"""

import socket, pdb

# Entonces mira, la idea es esta:   Tenemos que hacer conexion con los clientes en un chatroom.
# Despues de eso, nos enfocamos en crear como un master room, donde podemos ver todos los chatrooms. Por lo menos tengamos esa meta.
# Te parece?
CLIENTS = 12

# Funcion que permite agregar nuevos jugadores.
def create_socket(address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setblocking(0)
    s.bind(address)
    s.listen(CLIENTS)
    print("Now listening at ", address)
    return s

#Clase de un nuevo jugador
class Player:
    def __init__(self, socket, name) -> "newPlayer":
        socket.setblocking(0)
        self.socket = socket
        self.name = name
    
    def fileno(self):
        #Identificador de socket
        return self.socket.fileno()
#CLase de un room name
class roomGame:
    def __init__(self,name) -> 'NameRoom':
        #Cantidad de sockets/players que tendra un "chatroom"
        self.players = []
        self.name = name

    def greet_new_players(self, new_player):
        greeting = "Our game session" + self.name + "welcomes the new player named " + new_player.name + " ! \n"
        for player in self.players:
            player.socket.sendall(greeting.encode())
    
    def broadcast_messages(self, player, message):
        message = player.name.encode() + "Message to all: " + message + " \n"
        for player in self.players:
            player.socket.sendall(message)

    def remove_player(self, player):
        self.players.remove(player)
        leaving_message = player.name.encode() + "has left the game session. \n"
        self.broadcast_messages(player,leaving_message)

class gameServer:
    def __init__(self) -> "newGame":
        #Se haran diccionarios para dar lista de sesiones y que jugadores hay en esas sesiones
        self.gamerooms = {}
        self.gamerooms_platers = {}
    #Pendiente
    def greet_new_players_in_server(self, new_player):
        return 0
    def list_rooms(self,player):
        return 0
    def clien_menu():
        return 0
    def remove_player_in_server(self,player):
        return 0

