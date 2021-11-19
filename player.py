import json
from cards import cards
from dice import *

#Create dice
dice1 = dice
dice2 = dice
comm = cards(1)
chance = cards(2)
Comm_Cards = list(range(1,17))
random.shuffle(Comm_Cards)
Chnc_Cards = list(range(1,17))
random.shuffle(Chnc_Cards)


#loads master json file
a_file = open("Board.json", "r")
board = json.load(a_file)
a_file.close()


class player:
    #Global Variables
    space = 0
    jail = 1
        
    #Gives info on player position
    def status():
        print("Player is on", board["Space"][player.space]["Title"])

    #Updates players location based on previous location
    def space_update(totalRoll):
        player.space = (player.space + totalRoll)%40
        board["Space"][player.space]["Landed"]+=1
        a_file = open("Board_updated.json", "w")
        json.dump(board, a_file)
        a_file.close()

    #Updates player location
    def space_hardupdate(move):
        player.space = move
        board["Space"][player.space]["Landed"]+=1
        a_file = open("Board_updated.json", "w")
        json.dump(board, a_file)
        a_file.close()

    def turn(self, dicex, dicey):
        if player.jail == 3:
            player.space_hardupdate(10)
        else:
            player.space_update(dicex+dicey)
            if player.space == 2 or 17 or 33:
                draw = comm.draw(Comm_Cards)
                player.card_do(1, draw)
            elif player.space == 6 or 12 or 36:
                draw = chance.draw(Chnc_Cards)
                player.card_do(2, draw)    
            elif player.space == 30:
                player.space_hardupdate(10)
            if dicex == dicey:
                player.jail+=1
                player.turn(self, dice1.roll(), dice2.roll())
        player.jail = 1
            

    def card_do(flag, card):
        if card == 1:
            player.space_hardupdate(0)
        elif card == 2:
            player.space_hardupdate(10)
        elif card == 3 and flag == 2:
            player.space_hardupdate(39)
        elif card == 4 and flag == 2:
            player.space_hardupdate(24)
        elif card == 5 and flag == 2:
            player.space_hardupdate(11)
        elif card == 6 and flag == 2:
            player.space_hardupdate(5)  
        elif card == (7 or 8) and flag == 2:
            if player.space == 7:
                player.space_hardupdate(15)
            elif player.space == 12:
                player.space_hardupdate(25) 
            elif player.space == 36:
                player.space_hardupdate(5)      
        elif card == 9 and flag == 2:
            if player.space == 7:
                player.space_hardupdate(12)
            elif player.space == 12:
                player.space_hardupdate(28) 
            elif player.space == 36:
                player.space_hardupdate(12) 
