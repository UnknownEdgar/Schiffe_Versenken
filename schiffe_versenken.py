#########################################################################################################
#                                       game: Schiffe versenken                                         #
#                            Prüfungsaufgabe Informatik TEA23 Programmentwurf                           #                       
#########################################################################################################
#                        authors: Edgar Malinowsky, Johannes Rudolph, Tom Gluth                         #
#########################################################################################################


#########################################################################################################
#                                              Description                                              #
#                             the description can be found in the README file                           #
#########################################################################################################


# symbols of the game

#       X = hit
#       O = miss / non placable point
#       # = ship
#   space = water/placeholder

# colors

#       X = red
#       O = blue (miss)
#       O = dark grey (non placable point)
#       # = green

# comments

#       c: = color: 


# import of all requiered modules/files
import converter as cv
import ausgabe as au
import aufbau as af

# constants
FIELD_SIZE = 100
GRID = 10

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


# programm loop
while keep_going:

    # initialization of victory
    victory = False

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
    print("Spieler 1 ist dran:")
    af.aufbau(field_1, FIELD_SIZE, GRID)
    print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")  # create empty space
    print("Spieler 2 ist dran:") 
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
        au.print_field(active_shot_field, GRID, FIELD_SIZE)                         # Show the shot field of the active player
        
        print("Auf welches Feld möchten Sie schießen?")                 # get the shot coordinates by the player
    
        shot = cv.grid_conversion()                                     # convert the coordinates to the array index

        #####################################################################
            # hit detection

        if active_field[shot] == "\033[32m" + "#" + "\33[00m":                # Check if the shot hit a ship(#)
            hit = True                        
            active_shot_field[shot] = "\033[31m" + "X" + "\033[00m"           # mark corresponding field as a hit(X) colored red
            active_field[shot] = "\033[31m" + "X" + "\033[00m"                # mark hit of the ship in the enemies field colored red
            print("Der Schuss hat" + "\033[31m" + " getroffen!" + "\033[00m")
                                     # c: red                     c: white

        elif active_field[shot] != "\033[32m" + "#" + "\33[00m":              # Check if the shot missed a ship(#)
            hit = False 
            active_shot_field[shot] = "\033[36m" + "O" + "\033[00m"           # mark corresponding field as a miss(O) colored turquoise
            active_field[shot] = "\033[36m" + "O" + "\033[00m"                # mark miss in the enemies field colored turquoise
            print("Der Schuss ging" + "\033[36m" + " daneben!" + "\033[00m")  # print miss with "daneben" printed blue
                                      # c: blue                  c: white

        #######################################################################
            # Check for victory
        
        ships_left = 0

        for i in range(FIELD_SIZE):
            if active_field[i] == "\033[32m" + "#" + "\33[00m":              # Check if a ship(#) is still on the active grid
                ships_left += 1                                              # count up the counter ships_left by one
        
        if ships_left == 0:                                                  # when counter didn't count up -> no more ship on grid
            victory = 1                                                      # set feedback that one player won and the game shall stop

        ########################################################################
            # Switch active player

        if hit == False and active_player == 1:     # switch player two to be active when the shot missed
            active_player = 2
        
        elif hit == False and active_player == 2:   # switch player one to be active when the shot missed
            active_player = 1

        keep_going_loop = 0
        while keep_going_loop != 1 and ships_left != 0:
            keep_going_loop = 1
            check_self = 0
            try:
                check_self = int(input("Möchtest du dein eigenes Feld noch mal sehen?\n" + "\033[31m" + "0 Nein\n" + "\033[32m" + "1 Ja" + "\33[00m" + "\n"))   # give the active player the opportunity to look at his own field
            except ValueError:                                                             # c: red                  # c: green            # c: white
                keep_going_loop = 0   
            if check_self == 1:                                                                         # print own field when player demands to see it
                print("Deine Schiffe:")
                au.print_field(own_field, GRID, FIELD_SIZE)
                check_self = 0
            elif check_self > 1:
                keep_going_loop = 0
                print("Falsche Eingabe (0/1)")
            
        
        pause = input("Beliebige Taste drücken, um fortzufahren")
        print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")              # create empty space  

        if hit == True and ships_left != 0:
            print(f"Spieler {active_player} hat" + "\033[31m" + " getroffen" + "\033[00m" + " und darf nochmal schießen.")
                                                   # c: red                    c: white

    ################################################################################################
    '''output victory and winner'''
    ################################################################################################

    if victory == 1:
        print("Herzlichen Glückwunsch!!! \n" + "\033[1;33m" + "Spieler " + f"{active_player}" + "\033[00m" + " hat" + "\033[32m" + " gewonnen!" + "\33[00m")
                                               # c: yellow                                      c: white              c: green                    c: white    
          
    ################################################################################################
    '''check for end of playing'''
    ################################################################################################
    go_on = 0
    while go_on != 1:
        go_on = 1
        continue_play = 0
        try:
            continue_play = int(input("Wollen Sie eine weitere Runde spielen?\n" + "\033[31m" + "0 Nein\n" + "\033[32m" + "1 Ja" + "\33[00m" + "\n"))
        except ValueError:                                                         # c: red                  c: green              c: white
            go_on = 0
        if continue_play == 1:
            keep_going = 1
        elif continue_play > 1:
            go_on = 0
            print("Falsche Eingabe (0/1)")
        else:
            keep_going = 0