import os
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from player import *
from dice import *
players = []
dice1 = dice
dice2 = dice

def main():
    #Grab # of players and iterations from user
    player_input = int(input("Number of Players: "))
    iterations = int(input("Number of Iterations: "))
    for x in range(player_input):
        players.append(player())

    # removes temp json file
    if os.path.exists("Board_updated.json"):
        os.remove("Board_updated.json")
    else:
        print("Nothing to delete")

    #Play the Game with a set amount of turns
    for x in range (iterations):
        for obj in players:
            obj.turn(dice1.roll(),dice2.roll())
    
    #read json file
    a_file = open("Board_updated.json", "r")
    board = json.load(a_file)
    a_file.close()

    # Create Arrays for Graph
    spaces = board["Space"]
    total = []
    landed = []
    total_ROI = []
    #Create the Colors array
    for color in spaces:
        total.append(color["Color"])

    #removes duplicate colors    
    colors= list(set(total))
    
    #Create the Landed Array
    for x in colors:
        Total_landed = 0
        ROI = 0
        for color in spaces:
            if color["Color"] == x:
                ROI = ROI + (color["Landed"]*color["Pay"])
                Total_landed = Total_landed + color["Landed"]
        total_ROI.append(ROI)      
        landed.append(Total_landed)   

    #Create Dataset
    df = pd.DataFrame({"Colors": colors, "Landed": landed, "ROI": total_ROI})
    df1 = df.sort_values("ROI")
    omit = ["None","Community","Chance"]
    index = df1[(df1["Colors"] == "None") | (df1["Colors"] == "Community") | (df1["Colors"] == "Chance")].index
       
    # Plot Bar Graph 
    plt.subplot(1,2,1)
    plt.barh("Colors","Landed",data=df1.drop(index))
    plt.xlabel("Landed")
    plt.ylabel("Color")
    plt.subplot(1,2,2)
    plt.barh("Colors","ROI",data=df1.drop(index))
    plt.xlabel("ROI")
    plt.ylabel("Color")
    plt.show()

    print("Done")




        
    


    
        
        

    


if __name__ == "__main__":
    main()