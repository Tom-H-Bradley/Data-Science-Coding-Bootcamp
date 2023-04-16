#Importing the random module, which will allow the program to generate a random grid for the user to play

import random

rows = int(input("How many rows would you like the grid to have?"))
columns = int(input("How many columns would you like the grid to have?"))

#By setting the amount of mines we are randomly selecting from, we can control the difficulty of the game. 
#In this case I have chosen a ratio of 4:1 difficulty. the random attribute may still generate a grid of all mines, but this will be
#less likely

mine = ["#", "-", "-", "-"]

#The below loop generates a grid based on the amount of row and columnd the user has selected, and using the random module which
#I researched on the Geeks for Geeks website, selects all the values. This uses a nested loop to generate the 2D array.

grid = []
for row in range(rows):
    list = []
    for column in range(columns):
        entry = random.choice(mine)
        list.append(entry)
    grid.append(list)

#The visible grid is what the user will see, we don't want the location of the mines to be visible. Therefore we need a grid identical
#in size and dimension to the actual grid, that we can print eh answers to later on in the game.

visible_grid = []
for row in range(rows):
    list = []
    for column in range(columns):
        list.append("O")
    visible_grid.append(list)

print(visible_grid)

#The while loop below, allows the game to continue indefinitely until the user selects a mine. at this point the Boolean will 
#switch to false and the loop will stop and print out a statement.

in_game = True
while in_game:
    rselection = int(input("What row are you selecting?")) - 1
    cselection = int(input("What column are you selecting?")) - 1
    if grid[rselection][cselection] == "#":
        print("You have lost!")
        in_game = False
    #The below loop looks at every adjacent location to the area selected by the user. Code has been added to prevent the lists from 
    #working on a cyclical basis. I.e. if rselection + i is equal to the length of the grid then this will add 0 to the count 
    elif grid[rselection][cselection] == "-":
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if rselection + i == len(grid) or rselection + i == 0 or cselection + j == len(grid[rselection]) or cselection + j == 0:
                    count += 0            
                elif grid[rselection + i][cselection+j] == "#":
                    count += 1
        #we apply the same code to the visible grid nd the actual grid, which means that they become a mirror of each other
        grid[rselection][cselection] = count
        visible_grid[rselection][cselection] = count
    else:
        print("You have already selected here")
    print(visible_grid)

#At the bottom, we print the visible grid every time so the user can select another value.

        
