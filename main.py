import os
import json
import matplotlib.pyplot as plt
import numpy as np
from player import *
from dice import *
player1 = player("Jason")
dice1 = dice
dice2 = dice

def main():
    
    # removes temp json file
    if os.path.exists("Board_updated.json"):
        os.remove("Board_updated.json")
    else:
        print("Nothing to delete")

    #Play the Game with a set amount of turns
    for x in range (1000):
        player1.turn(dice1.roll(),dice2.roll())
    
    #read json file
    a_file = open("Board_updated.json", "r")
    board = json.load(a_file)
    a_file.close()

    # Create Arrays for Graph
    spaces = []
    landed = []
    color = []

    #Add data from json file to arrays
    for x in range(40):
        spaces.append(board["Space"][x]["Title"])
        landed.append(board["Space"][x]["Landed"])
        color.append(board["Space"][x]["Type"]["Color"])
    
    # Plot Bar Graph 
    plt.barh(color,landed)
    plt.xlabel("Landed")
    plt.ylabel("Color")
    plt.show()




        
    


    
        
        

    


if __name__ == "__main__":
    main()