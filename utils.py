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
PORT = 5555
quitting = "QUIT"

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
        #name = input("Ingrese el nombre para su jugador: ")
        self.name = name
        self.status = "Online"

    def fileno(self):
        #Identificador de socket
        return self.socket.fileno()
    def setName(self, name):
        self.name = name

    def toggleStatus(self):
        if self.status == "Online":
            self.status = "Offline"
        else:
            self.status = "Online"

#CLase de un room name
class roomGame:
    def __init__(self,name) -> 'NameRoom':
        #Cantidad de sockets/players que tendra un "chatroom"
        self.players = []
        self.name = name

    def greet_new_players(self, new_player):
        greeting = "Our game session " + self.name + "  welcomes the new player named " + new_player.name + " ! \n"
        greeting = bytes(greeting, "utf8")
        for player in self.players:
            player.socket.sendall(greeting)

    def broadcast_messages(self, player, message):
        message = str(player.name) + " sends message to all:  " + str(message) + " \n"
        message = bytes(message, "utf8")
        for player in self.players:
            player.socket.sendall(message)

    def remove_player(self, player):
        self.players.remove(player)
        leaving_message = player.name + " has left the game session. \n"
        leaving_message = bytes(leaving_message, "utf8")
        self.broadcast_messages(player,leaving_message)

class gameServer:
    def __init__(self) -> "newGame":
        #Se haran diccionarios para dar lista de sesiones y que jugadores hay en esas sesiones
        self.gamerooms = {}
        self.gamerooms_players = {}
    #Saluda a nuevos jugadores en el servidor
    def greet_new_players_in_server(self, new_player):
        new_player.socket.sendall(b"Welcome to the Game Server ! \n")
        new_player.socket.sendall(b"Apache enter para continuar")
        #print()


    def list_rooms(self,player):
        #muestra todos los gamerooms
        print("LENGHT = " + str(len(self.gamerooms)))
        if int(len(self.gamerooms)) == 0:
            message = b"There's 0 game sessions right now... \n Create your own game room! \n Type [join room_name] to create a room. \n"
            player.socket.sendall(message)
        else:
            message = "Listing all current game sessions... \n"
            message = bytes(message, "utf8")
            for room in self.gamerooms:
                print("Room: " +str(room))
                message = room + ":  " + str(len(self.gamerooms[room].players)) + " player(s) \n "
                message = bytes(message, "utf8")
                player.socket.sendall(message)



    # def new_client(self, player, command):

    def remove_player_in_server(self,player):
        if player.name in self.gamerooms_players:
            self.gamerooms[self.gamerooms_players[player.name]].remove_player(player)
            del self.gamerooms_players[player.name]
        print("Player: " + player.name + " has left \n")

    def client_menu(self, player, command):
        #Menu principal

        menu = b"""
        |-----------------------------------|
        Welcome to the Game Server ! \n
        write [NAME your_name] to set your name \n
        write [TOGGLE] to change your status to online/offline \n
        write [LIST] to have a list of all Game Rooms \n
        write [JOIN gameRoom_name] to join/create/switch to another game room \n
        write [MANUAL] to show again the commands \n
        write [QUIT] to get out of the game server \n
        |-----------------------------------|
        \n
        """
        #command
        player.name = str(player.name)

        nose = player.name + " says: " + command

        print("COMMAND ==" + str(command))

        #print("\n")
        #print("NOSE == " + nose)
        #print("PLAYER NAME == " + str(player.name))
        if player.name in nose:
            print("\nName " + player.name + " \n")
            print("New connection from: ", player.name)
            player.socket.sendall(menu)

        if "JOIN" in command:
            same_gameroom = False
            if len(nose.split()) >= 2:
                room_name = command.split()[1]
                if player.name in self.gamerooms_players:
                    if self.gamerooms_players[player.name] == room_name:
                        player.socket.sendall("You're a already in room: " + room_name.encode())
                        same_gameroom = True
                    else:
                        old_gameroom = self.gamerooms_players[player.name]
                        self.gamerooms[old_gameroom].remove_player_in_server(player)
                if not same_gameroom:
                    if not room_name in self.gamerooms: #new game room
                        new_gameroom = roomGame(room_name)
                        self.gamerooms[room_name] = new_gameroom
                    self.gamerooms[room_name].players.append(player)
                    self.gamerooms[room_name].greet_new_players(player)
                    self.gamerooms_players[player.name] = room_name
            else:
                player.socket.sendall(menu)

        elif "LIST" in command:
            self.list_rooms(player)

        elif "MANUAL" in command:
            player.socket.sendall(menu)

        elif "TOGGLE" in command:
            player.toggleStatus()
            mensaje_toggle = "\nEl jugador " +player.name+ " cambio su status a "+ player.status+ ".\n "
            mensaje_toggle = bytes(mensaje_toggle, "utf8")
            player.socket.sendall(mensaje_toggle)


        elif "QUIT" in  command:
            player.socket.sendall(quitting.encode())
            self.remove_player_in_server(player)
        else:
            if player.name in self.gamerooms_players:
                self.gamerooms[self.gamerooms_players[player.name]].broadcast_messages(player, command)
            #else:
            #    message = b"""
            #        You're bad"""
            #    player.socket.sendall(message)
