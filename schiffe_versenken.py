#########################################################################################################
#                                       game: Schiffe versenken                                         #
#                            Prüfungsaufgabe Informatik TEA23 Pogrammentwurf                            #                       
#########################################################################################################
#                        authors: Edgar Mailinowsky, Johannes Rudolph, Tom Gluth                        #
#########################################################################################################


#########################################################################################################
#                                              Desciption                                               #
#                             the description can be found in the README file                           #
#########################################################################################################


# symbols of the game

#       X = hit
#       O = miss / non placable point
#       # = ship
#   space = water/placeholder

# import of all requiered modules/files
import converter as cv
import ausgabe as au
import aufbau as af

# constants
FIELD_SIZE = 25
GRID = 5

# common variables
active_field = []
active_player = 1           # active player playing the game
active_shot_field =[] 
field_1 = []
field_2 = []
hit = False
keep_going = True
player_shot = ""            # shot input by player 
shot = 0                    # shot input by player after grid convertion 
shotfield_1 = []
shotfield_2 = []
victory = False

# programm loop
while keep_going:

    # creating all arrays with SPACES
    af.gen_array(field_1, FIELD_SIZE)
    af.gen_array(field_2, FIELD_SIZE)
    af.gen_array(shotfield_1, FIELD_SIZE)
    af.gen_array(shotfield_2, FIELD_SIZE)

    # deleting already placed ships
    af.gen_empty(field_1, FIELD_SIZE)
    af.gen_empty(field_2, FIELD_SIZE)
    af.gen_empty(shotfield_1, FIELD_SIZE)
    af.gen_empty(shotfield_2, FIELD_SIZE)

    # creating ships in arrays
    print("Spieler 1 ist dran:\n")
    af.aufbau(field_1, FIELD_SIZE, GRID)
    print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")  # create empty space
    print("Spieler 2 ist dran:\n") 
    af.aufbau(field_2, FIELD_SIZE, GRID)
    print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")  # create empty space 

    ################################################################################################
    '''Shot Sequence'''
    ################################################################################################

    while victory == False:
        ####################################################################
            # active player check

        if active_player == 1:                  # Check which player is active and assign 
            active_field = field_2              # the corresponding fields to be active
            active_shot_field = shotfield_1
            own_field = field_1
        elif active_player == 2:
            active_field = field_1
            active_shot_field = shotfield_2
            own_field = field_2

        ####################################################################
            # shot input and conversion

        print(f"Spieler {active_player} ist dran.")                     # Show which player is active
        
        print("Deine Schüsse:")
        au.print_field(active_shot_field)                               # Show the shot field of the active player
        
        print("Auf welches Feld möchten Sie schießen?")                 # get the shot coordinates by the player
    
        shot = cv.grid_conversion()                                     # convert the coordinates to the array index

        #####################################################################
            # hit detection

        if active_field[shot] == "#":               # Check if the shot hit a ship(#)
            hit = True                        
            active_shot_field[shot] = "X"           # mark corresponding field as a hit(X)
            active_field[shot] = "X"                # mark hit of the ship in the enemies field
            print("Der Schuss hat getroffen!")

        elif active_field[shot] != "#":             # Check if the shot missed a ship(#)
            hit = False 
            active_shot_field[shot] = "O"           # mark corresponding field as a miss(O)
            active_field[shot] = "O"                # mark miss in the enemies field
            print("Der Schuss ging daneben!")

        #######################################################################
            # Check for victory
        
        counter = 0

        for i in range(25):
            if active_field[i] == "#":              # Check if a ship(#) is still on the active grid
                counter += 1                        # count up the counter by one
        
        if counter == 0:                            # when counter didn't count up -> no more ship on grid
            victory = 1                             # set feedback that one player won and the game shall stop

        ########################################################################
            # Switch active player

        if hit == False and active_player == 1:     # switch player two to be active when the shot missed
            active_player = 2
        
        elif hit == False and active_player == 2:   # switch player one to be active when the shot missed
            active_player = 1

        try:
            check_self = int(input("Möchtest du dein eigenes Feld noch mal sehen?\n0 Nein\n1 Ja\n "))   # give the active player the opportunity to look at his own field
        except ValueError:
            Error = True    
        if check_self == 1:                                                                             # print own field when player demands to see it
            print("Deine Schiffe:")
            au.print_field(own_field)
        
        check_self = 0
        
        pause = input("Beliebiege Taste drücken, um fortzufahren")
        print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")              # create empty space  

        if hit == True and counter != 0:
            print(f"Spieler {active_player} hat getroffen und darf nochmal schießen.")

    ################################################################################################
    '''output victory and winner'''
    ################################################################################################

    if victory == 1:
        print(f"Herzlichen Glückwunsch!!! \nSpieler {active_player} hat gewonnen!")

    ################################################################################################
    '''check for end of playing'''
    ################################################################################################

    if bool(input("Wollen Sie eine weitere Runde spielen? Nein(0), Ja(1)")):
        keep_going = 1
    else:
        keep_going = 0