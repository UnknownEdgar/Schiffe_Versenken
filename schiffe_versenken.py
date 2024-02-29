# symbols of the game

#       X = hit
#       O = miss
#       # = ship
#   space = water/placeholder

# common variables
active_field = []
active_player = 0           # active player playing the game
active_shot_field =[]       
field_1 = []
field_2 = []
hit = False
player_shot = ""            # shot input by player 
shot = 0                    # shot input by player after grid convertion 
shotfield_1 = []
shotfield_2 = []
victory = False



################################################################################################
'''Shot Sequence'''
################################################################################################

while victory == False:
    ####################################################################
        # active player check

    if active_player == 1:                  # Check which player is active and assign 
        active_field = field_2              # the corresponding fields to be active
        active_shot_field = shotfield_1
    elif active_player == 2:
        active_field = field_1
        active_shot_field = shotfield_2

    ####################################################################
        #shot input and conversion

    print(f"Spieler {active_player} ist dran.") # Show which player is active
    
    print_field(active_shot_field)              # Show the shot field of the active player
    
    player_shot = input("Auf welches Feld möchten Sie schießen?") # get the shot coordinates by the player
   


    shot = grid_conversion(player_shot)         # convert the coordinates to the array index

    #####################################################################
        # hit detection

    if active_field[shot] == "#":               # Check if the shot hit a ship(#)
        hit = True                        
        active_shot_field[shot] = "X"           # mark corresponding field as a hit(X)
        active_field[shot] = " "                # delete the ship in the enemies field
        print("Der Schuss hat getroffen!")

    elif active_field[shot] != "#":             # Check if the shot missed a ship(#)
        hit = False 
        active_shot_field[shot] = "O"           # mark corresponding field as a miss(O)
        print("Der Schuss ging daneben!")

    #######################################################################
        #Check for victory

    counter = 0
    
    for i in range(25):
        if active_field[i] == "#":              # Check if a ship(#) is still on the active grid
            counter += 1                        # count up the counter by one
    
    if counter == 0:                            # when counter didn't count up -> no more ship on grid
        victory = 1                             # set feedback that one player won and the game shall stop

    ########################################################################
        # Switch active player

    if hit == False and active_player == 1: # switch player two to be active when the shot missed
        active_player = 2

    if hit == False and active_player == 2: # switch player one to be active when the shot missed
        active_player = 1


    print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n") # create empty space for visualisation of new shot 

    if hit == True:
        print(f"Spieler {active_player} hat getroffen und darf nochmal schießen.")

################################################################################################
'''output victory and winner'''
################################################################################################

if victory == 1:
    print(f"Herzlichen Glückwunsch!!! \n Spieler {active_player} hat gewonnen!")






