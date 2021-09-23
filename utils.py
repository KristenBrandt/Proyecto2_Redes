"""
Universidad del Valle de Guatemala
Seccion 10
Ing. Jorge Yass
utils.py
Proposito: Funciones y clases para client y server
"""

import socket, pdb, random

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
class downTheRiver:
    def ascii_version_of_card(drawnCards, return_string=True):
        cards = []
        for l in range(len(drawnCards)):
            cards.append(drawnCards[l].copy())

        suits_name = ['S', 'D', 'H', 'C']
        suits_symbols = ['♠', '♦', '♥', '♣']

        for i in range(len(cards)):
            if int(cards[i][0]) == 11:
                cards[i][0] = "J"

            elif int(cards[i][0]) == 12:
                cards[i][0] = "Q"

            elif int(cards[i][0]) == 13:
                cards[i][0] = "K"

            elif int(cards[i][0]) == 1:
                cards[i][0] = "A"



        # create an empty list of list, each sublist is a line
        lines = [[] for i in range(9)]

        for i in range(len(cards)):
            ten = False


            rank = cards[i][0]
            suit = suits_name.index(cards[i][1])
            suit = suits_symbols[suit]

            if cards[i][0] == "10":
                ten = True
                space = ""
            else:
                space = " "

            lines[0].append('┌─────────┐')
            if ten:
                lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
            else:
                lines[1].append('│{}{}       │'.format(rank, space))  # use two {} one for char, one for space or char
            lines[2].append('│         │')
            lines[3].append('│         │')
            lines[4].append('│    {}    │'.format(suit))
            lines[5].append('│         │')
            lines[6].append('│         │')
            if ten:
                lines[7].append('│       {}{}│'.format(rank, space))
            else:
                lines[7].append('│       {}{}│'.format(space, rank))
            lines[8].append('└─────────┘')

        result = []
        for index, line in enumerate(lines):
            result.append(''.join(lines[index]))

        # hidden cards do not use string
        if return_string:
            return '\n'.join(result)
        else:
            return result


    def pullCard(deck, drawn):
        index = random.randint(0, len(deck)-1)
        card = deck.pop(index)
        drawn.append(card)

    def checkFill(deck):
        if len(deck)<1:
            deck = [["1","S"], ["2","S"], ["3","S"], ["4","S"], ["5","S"], ["6","S"], ["7","S"], ["8","S"], ["9","S"], ["10","S"], ["11","S"], ["12","S"], ["13","S"],

                ["1","H"], ["2","H"], ["3","H"], ["4","H"], ["5","H"], ["6","H"], ["7","H"], ["8","H"], ["9","H"], ["10","H"], ["11","H"], ["12","H"], ["13","H"],

                ["1","C"], ["2","C"], ["3","C"], ["4","C"], ["5","C"], ["6","C"], ["7","C"], ["8","C"], ["9","C"], ["10","C"], ["11","C"], ["12","C"], ["13","C"],

                ["1","D"], ["2","D"], ["3","D"], ["4","D"], ["5","D"], ["6","D"], ["7","D"], ["8","D"], ["9","D"], ["10","D"], ["11","D"], ["12","D"], ["13","D"]]
            print("\nEl deck fue renovado...\n")
            return deck
        return deck
    def redBlack(drawn, ans):
        ind = len(drawn) - 1

        if drawn[ind][1] == "D" or drawn[ind][1] == "H":
            if ans == 'red':
                return True
        elif drawn[ind][1] == "S" or drawn[ind][1] == "C":
            if ans == 'black':
                return True
        return False

    def upDown(drawn, ans):
        ind = len(drawn) - 1
        if int(drawn[ind][0]) > int(drawn[ind-1][0]) and ans == "up":
            return True
        elif int(drawn[ind][0]) < int(drawn[ind-1][0]) and ans == "down":
            return True
        else:
            return False

    def inOut(drawn, ans):
        ind = len(drawn) - 1
        dr = int(drawn[ind][0])

        dr1 = int(drawn[ind-1][0])

        dr2 = int(drawn[ind-2][0])

        mini = min(dr1, dr2)

        maxi = max(dr1, dr2)

        ran = range(mini, maxi+1)

        if dr in ran and ans == "in":
            return True
        elif dr not in ran and ans == "out":
            return True
        else:
            return False

    def symb(drawn, ans):
        ind = len(drawn) - 1
        if drawn[ind][1] == ans:
            return True
        else:
            return False

    def mainmenu():
        menu =
            '''
            ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O


            Elija el numero de jugadores:

            1. Un jugador
            2. Dos jugadores
            3. Tres jugadores
            4. Cuatro jugadores
            0. Salir del juego (En cualquier pregunta se puede salir respondiendo 0)

            ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O

            '''
        return menu

    def choosepoints():
        print(
            '''
            ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O

            Elija cantidad de puntos para perder:

            1. 15 puntos
            2. 30 puntos
            3. 45 puntos

            ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O
        ''')

    def round1():
        r1 =
        '''
        Rojo o negro?
        1. Rojo
        2. Negro

        '''
        return r1

    def round2():

        r2 =
        '''
        Arriba o abajo?
        1. Arriba
        2. Abajo

        '''
        return r2

    def round3():

        r3 =
        '''
        Adentro o afuera?
        1. Adentro
        2. Afuera

        '''
        return r3

    def round4():

        r4 =
        '''
        Combo o pass?
        1. Combo
        2. Pass

        '''
        return r4

    def roundC():
        # para cliente y/o ser
        rC =
        '''
        Elije un simbolo:
        1. Heart (H)
        2. Spade (S)
        3. Diamond (D)
        4. Clover (C)

        '''
        return rC

    def defendIn(num):
        # Para cliente
        correct = False
        textinput = input()
        while not correct:
            try:
                textinput = int(textinput)
                if textinput < 0 or textinput > num:
                    print("\nPor favor elija un numero valido...\n")
                else:
                    correct = True
                    return textinput
            except:
                print("\nPor favor elija un numero valido...\n")
            textinput = input("Ingrese un numero de 0-"+str(num)+": ")



class roomGame:
    def __init__(self,name) -> 'NameRoom':
        #Cantidad de sockets/players que tendra un "chatroom"
        self.players = []
        self.name = name
        self.dtr = downTheRiver()
        self.points = 2
        self.playersInSesion = {}
        self.deck = [["1","S"], ["2","S"], ["3","S"], ["4","S"], ["5","S"], ["6","S"], ["7","S"], ["8","S"], ["9","S"], ["10","S"], ["11","S"], ["12","S"], ["13","S"],
            ["1","H"], ["2","H"], ["3","H"], ["4","H"], ["5","H"], ["6","H"], ["7","H"], ["8","H"], ["9","H"], ["10","H"], ["11","H"], ["12","H"], ["13","H"],
            ["1","C"], ["2","C"], ["3","C"], ["4","C"], ["5","C"], ["6","C"], ["7","C"], ["8","C"], ["9","C"], ["10","C"], ["11","C"], ["12","C"], ["13","C"],
            ["1","D"], ["2","D"], ["3","D"], ["4","D"], ["5","D"], ["6","D"], ["7","D"], ["8","D"], ["9","D"], ["10","D"], ["11","D"], ["12","D"], ["13","D"]]
        self.drawn = []
        self.turn = False
        self.maxPoints = 20
        self.dead = []

    def greet_new_players(self, new_player):
        greeting = "Our game session " + self.name + "  welcomes the new player named " + new_player.name + " ! \n"
        greeting = bytes(greeting, "utf8")
        welcome = b"""




   _   _   _   _   _   _   _     _   _
  / \ / \ / \ / \ / \ / \ / \   / \ / \
 ( W ( e ( l ( c ( o ( m ( e ) ( t ( o )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/


.------.------.------.------.     .------.------.------.     .------.------.------.------.------.
|D.--. |O.--. |W.--. |N.--. |.-.  |T.--. |H.--. |E.--. |.-.  |R.--. |I.--. |V.--. |E.--. |R.--. |
| :/\: | :/\: | :/\: | :(): ((5)) | :/\: | :/\: | (\/) ((5)) | :(): | (\/) | :(): | (\/) | :(): |
| (__) | :\/: | :\/: | ()() |'-.-.| (__) | (__) | :\/: |'-.-.| ()() | :\/: | ()() | :\/: | ()() |
| '--'D| '--'O| '--'W| '--'N| ((1)| '--'T| '--'H| '--'E| ((1)| '--'R| '--'I| '--'V| '--'E| '--'R|
`------`------`------`------'  '-'`------`------`------'  '-'`------`------`------`------`------'





    """
        new_player.socket.sendall(welcome)
        for player in self.players:
            player.socket.sendall(greeting)

    def broadcast_messages(self, player, message):
        message = str(player.name) + " sends message to all:  " + str(message) + " \n"
        message = bytes(message, "utf8")
        for player in self.players:
            player.socket.sendall(message)

    def broadcast_server_messages(self, message):
        message = bytes(message)
        for player in self.players:
            player.socket.sendall(message)

    def startGame(self):
        self.playersInSesion = {}
        for pl in self.players:
            self.playersInSesion[pl.name] = 0
        self.points = 2
        self.deck = [["1","S"], ["2","S"], ["3","S"], ["4","S"], ["5","S"], ["6","S"], ["7","S"], ["8","S"], ["9","S"], ["10","S"], ["11","S"], ["12","S"], ["13","S"],
            ["1","H"], ["2","H"], ["3","H"], ["4","H"], ["5","H"], ["6","H"], ["7","H"], ["8","H"], ["9","H"], ["10","H"], ["11","H"], ["12","H"], ["13","H"],
            ["1","C"], ["2","C"], ["3","C"], ["4","C"], ["5","C"], ["6","C"], ["7","C"], ["8","C"], ["9","C"], ["10","C"], ["11","C"], ["12","C"], ["13","C"],
            ["1","D"], ["2","D"], ["3","D"], ["4","D"], ["5","D"], ["6","D"], ["7","D"], ["8","D"], ["9","D"], ["10","D"], ["11","D"], ["12","D"], ["13","D"]]
        self.turn = False
        broadcast_server_messages(self, "!!!!!\n\nRecuerde que ♥ y ♦ son rojos \n\ty\nrecuerde que ♠ y ♣ son negros...\n\n\t\t\t!!!!!")
        #print("!!!!!\n\nRecuerde que ♥ y ♦ son rojos \n\ty\nrecuerde que ♠ y ♣ son negros...\n\n\t\t\t!!!!!")
        while(turn):

            dead = []
            if len(self.playersInSesion) == 1:
                for key in self.playersInSesion:
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    print("Felicidades " + key + "\n\nHas ganado!\n\n")
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    self.turn = False
                    break
            for player in self.playersInSesion:
                self.drawn = []
                #Round 1 comienza
                print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                print("Le toca a "+ player + "\n")
                print("Con " + str(self.playersInSesion[player])+ " puntos.\n")
                print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                self.dtr.round1()
                ans = self.dtr.defendIn(2)
                print("\nPulling Card...\n")
                self.dtr.pullCard(self.deck, self.drawn)
                self.deck = self.dtr.checkFill(self.deck)
                print(self.dtr.ascii_version_of_card(self.drawn))
                if ans == 1:
                    if redBlack(self.drawn, "red"):
                        print("Bien hecho!\nContinuando...\n")
                        self.points = self.points + 2
                    else:
                        print("Perdiste "+ player +" :(")
                        print("\nRecibes " + str(self.points) + " puntos...\n")
                        self.playersInSesion[player] = self.playersInSesion[player] + self.points
                        if self.playersInSesion[player] >= self.maxPoints:
                            print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                            if len(self.playersInSesion) != 1:
                                    self.dead.append(player)
                        print('\nPasando a siguiente jugador\n')
                        self.points = 2
                        continue

                elif ans == 2:
                    if self.dtr.redBlack(self.drawn, "black"):
                        print("Bien hecho!\nContinuando...\n")
                        self.points = self.points + 2
                    else:
                        print("Perdiste "+ player +" :(")
                        print("\nRecibes " + str(self.points) + " puntos...\n")
                        self.playersInSesion[player] = self.playersInSesion[player] + self.points
                        if self.playersInSesion[player] >= self.maxPoints:
                            print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                            if len(self.playersInSesion) != 1:
                                    self.dead.append(player)
                        print('\nPasando a siguiente jugador\n')
                        self.points = 2
                        continue
                elif ans == 0:
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    print("\nCerrando juego...\n")
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    self.turn = False
                    break

                #Round 2 comienza
                self.dtr.round2()
                ans = self.dtr.defendIn(2)
                print("\nPulling Card...\n")
                pullCard(self.deck, self.drawn)
                self.deck = checkFill(self.deck)
                print(self.dtr.ascii_version_of_card(self.drawn))

                if ans == 1:
                    if self.dtr.upDown(self.drawn, "up"):
                        print("Bien hecho!\nContinuando...\n")
                        self.points = self.points + 2
                    else:
                        print("Perdiste "+ player +" :(")
                        print("\nRecibes " + str(self.points) + " puntos...\n")
                        self.playersInSesion[player] = self.playersInSesion[player] + self.points
                        if self.playersInSesion[player] >= self.maxPoints:
                            print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                            if len(self.playersInSesion) != 1:
                                    self.dead.append(player)
                        print('\nPasando a siguiente jugador\n')
                        self.points = 2
                        continue
                elif ans == 2:
                    if self.dtr.upDown(self.drawn, "down"):
                        print("Bien hecho!\nContinuando...\n")
                        self.points = self.points + 2
                    else:
                        print("Perdiste "+ player +" :(")
                        print("\nRecibes " + str(self.points) + " puntos...\n")
                        self.playersInSesion[player] = self.playersInSesion[player] + self.points
                        if self.playersInSesion[player] >= self.maxPoints:
                            print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                            if len(self.playersInSesion) != 1:
                                    self.dead.append(player)
                        print('\nPasando a siguiente jugador\n')
                        self.points = 2
                        continue
                elif ans == 0:
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    print("\nCerrando juego...\n")
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    self.turn = False
                    break

                 #Round 3 comienza
                self.dtr.round3()
                ans = self.dtr.defendIn(2)
                print("\nPulling Card...\n")
                self.dtr.pullCard(self.deck, self.drawn)
                self.deck = self.dtr.checkFill(self.deck)
                print(self.dtr.ascii_version_of_card(self.drawn))

                if ans == 1:
                    if self.dtr.inOut(self.drawn, "in"):
                        print("Bien hecho!\nContinuando...\n")
                        self.points = self.points + 1
                    else:
                        print("Perdiste "+ player +" :(")
                        print("\nRecibes " + str(self.points) + " puntos...\n")
                        self.playersInSesion[player] = self.playersInSesion[player] + self.points
                        if self.playersInSesion[player] >= self.maxPoints:
                            print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                            if len(self.playersInSesion) != 1:
                                    self.dead.append(player)
                        print('\nPasando a siguiente jugador\n')
                        self.points = 2
                        continue
                elif ans == 2:
                    if self.dtr.inOut(self.drawn, "out"):
                        print("Bien hecho!\nContinuando...\n")
                        self.points = self.points + 1
                    else:
                        print("Perdiste "+ player +" :(")
                        print("\nRecibes " + str(self.points) + " puntos...\n")
                        self.playersInSesion[player] = self.playersInSesion[player] + self.points
                        if self.playersInSesion[player] >= self.maxPoints:
                            print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                            if len(self.playersInSesion) != 1:
                                    self.dead.append(player)
                        print('\nPasando a siguiente jugador\n')
                        self.points = 2
                        continue
                elif ans == 0:
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    print("\nCerrando juego...\n")
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    self.turn = False
                    break

                #Round 4 comienza
                self.dtr.round4()
                ans = self.dtr.defendIn(2)
                if ans == 1:
                    # Round C comienza
                    self.dtr.roundC()
                    ans = self.dtr.defendIn(4)

                    print("\nPulling Card...\n")
                    self.dtr.pullCard(self.deck, self.drawn)
                    self.deck = self.dtr.checkFill(self.deck)
                    print(self.dtr.ascii_version_of_card(self.drawn))

                    if ans == 1:
                        if self.dtr.symb(self.drawn, "H"):
                            print("Bien hecho!\nContinuando...\n")
                            self.points = self.points * 2
                        else:
                            print("Perdiste "+ player +" :(")
                            print("\nRecibes " + str(self.points) + " puntos...\n")
                            self.playersInSesion[player] = self.playersInSesion[player] + self.points
                            if self.playersInSesion[player] >= self.maxPoints:
                                print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                                if len(self.playersInSesion) != 1:
                                        self.dead.append(player)
                            print('\nPasando a siguiente jugador\n')
                            self.points = 2
                            continue
                    elif ans == 2:
                        if self.dtr.symb(self.drawn, "S"):
                            print("Bien hecho!\nContinuando...\n")
                            self.points = self.points * 2
                        else:
                            print("Perdiste "+ player +" :(")
                            print("\nRecibes " + str(self.points) + " puntos...\n")
                            self.playersInSesion[player] = self.playersInSesion[player] + self.points
                            if self.playersInSesion[player] >= self.maxPoints:
                                print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                                if len(self.playersInSesion) != 1:
                                        self.dead.append(player)
                            print('\nPasando a siguiente jugador\n')
                            self.points = 2
                            continue
                    elif ans == 3:
                        if self.dtr.symb(self.drawn, "D"):
                            print("Bien hecho!\nContinuando...\n")
                            self.points = self.points * 2
                        else:
                            print("Perdiste "+ player +" :(")
                            print("\nRecibes " + str(self.points) + " puntos...\n")
                            self.playersInSesion[player] = self.playersInSesion[player] + self.points
                            if self.playersInSesion[player] >= self.maxPoints:
                                print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                                if len(self.playersInSesion) != 1:
                                        self.dead.append(player)
                            print('\nPasando a siguiente jugador\n')
                            self.points = 2
                            continue
                    elif ans == 4:
                        if self.dtr.symb(self.drawn, "C"):
                            print("Bien hecho!\nContinuando...\n")
                            self.points = self.points * 2
                        else:
                            print("Perdiste "+ player +" :(")
                            print("\nRecibes " + str(self.points) + " puntos...\n")
                            self.playersInSesion[player] = self.playersInSesion[player] + self.points
                            if self.playersInSesion[player] >= self.maxPoints:
                                print("Oh noo!\n" + player+ " ha llegado a " + str(self.playersInSesion[player]) + " puntos y debe retirarse.\nBye!")
                                if len(self.playersInSesion) != 1:
                                        self.dead.append(player)
                            print('\nPasando a siguiente jugador\n')
                            self.points = 2
                            continue
                    elif ans == 0:
                        print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                        print("\nCerrando juego...\n")
                        print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                        self.turn = False
                        break
                elif ans == 2:
                    print('\nPasando a siguiente jugador\n')

                elif ans == 0:
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    print("\nCerrando juego...\n")
                    print("~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ~ o ~ O ")
                    self.turn = False
                    break
            if len(self.dead) > 0:
                for i in range(len(self.dead)):
                    self.playersInSesion.pop(self.dead[i])

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
