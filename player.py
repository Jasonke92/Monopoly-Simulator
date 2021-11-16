import json
from dice import *

#Create dice
dice1 = dice
dice2 = dice

#loads master json file
a_file = open("Board.json", "r")
board = json.load(a_file)
a_file.close()


class player:
    #Global Variables
    space = 0
    jail = 1

    #Create Fields
    def __init__(self, name):
        self.name = name
    
        
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
    def scace_hardupdate(move):
        player.space = move
        board["Space"][player.space]["Landed"]+=1
        a_file = open("Board_updated.json", "w")
        json.dump(board, a_file)
        a_file.close()

    #Rolls the dice and moves player
    def turn(self, dicex, dicey):
        if dicex == dicey:
            if player.jail < 3:
                player.space_update(dicex+dicey)
                player.jail+=1
                player.turn(self, dice1.roll(), dice2.roll())
            else:
                player.scace_hardupdate(10)
        else:
            player.space_update(dicex+dicey)
            player.jail = 1
            
