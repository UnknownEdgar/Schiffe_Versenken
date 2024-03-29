#########################################################################################################
#                                                                                                       #
#                                       game: Schiffe versenken                                         #
#                            Prüfungsaufgabe Informatik TEA23 Programmentwurf                           #
#                                                                                                       #                       
#########################################################################################################
#                                                                                                       #
#                        authors: Edgar Malinowsky, Johannes Rudolph, Tom Gluth                         #
#                                                                                                       #
#########################################################################################################


#########################################################################################################
#                                              Description                                              #
#                             the description can be found in the README file                           #
#########################################################################################################


# symbols of the game

#       X = hit
#       O = miss / non placable point
#       # = ship
#   space = water / placeholder

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
active_field = []           # currently used play-field 
active_player = 1           # active player playing the game
active_shot_field =[]       # currently used shot-field
continue_play = 1           # true when another round wants to be played
field_1 = []                # play-field of player 1
field_2 = []                # play-field of player 2
hit = False                 # true when shot hit a ship 
player_shot = ""            # shot input by player 
ships_left = 0              # amount of ships-pieces left in a play-field  
shot = 0                    # shot input by player after grid convertion 
shotfield_1 = []            # shot-field by player 1
shotfield_2 = []            # shot-field by player 2
victory = False             # true when a player has won the game 
wrong_input = False         # true when a wrong input occures


#########################################################################################################
#                                           main-game-loop                                              #
#                                                                                                       #
#########################################################################################################

while continue_play == 1:

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

    # creating ships in arrays and an empty space between the players turns
    print("Spieler 1 ist dran:")
    af.aufbau(field_1, FIELD_SIZE, GRID)
    input("Aufbau Spieler 1 abgeschlossen\nBeliebige Taste drücken, um fortzusetzen")
    print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")
    print("Spieler 2 ist dran:") 
    af.aufbau(field_2, FIELD_SIZE, GRID)
    input("Aufbau Spieler 2 abgeschlossen\nBeliebige Taste drücken, um fortzusetzen")
    print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")


    #####################################################################################################
    '''Shot Sequence'''
    #####################################################################################################

    while victory == False:


        #################################################################################################
        # active player check

        # check which player is active and assign the corresponding fields to be active
        if active_player == 1:                  
            active_field = field_2
            active_shot_field = shotfield_1
            own_field = field_1
        elif active_player == 2:
            active_field = field_1
            active_shot_field = shotfield_2
            own_field = field_2


        #################################################################################################
            # shot input and conversion

        # show which player is active
        print(f"Spieler {active_player} ist dran.")                     
        
        # show the shot field of the active player
        print("Deine Schüsse:")
        au.print_field(active_shot_field, GRID, FIELD_SIZE)             
        
        # get the shot coordinates by the player
        print("Auf welches Feld möchten Sie schießen?")
        shot = cv.grid_conversion(GRID)                                 


        #################################################################################################
            # hit detection

        # check if the shot hit a ship(#)
        if active_field[shot] == "\033[32m" + "#" + "\33[00m":                
            hit = True                        
            active_shot_field[shot] = "\033[31m" + "X" + "\033[00m"           # mark corresponding field as a hit(X) colored red
            active_field[shot] = "\033[31m" + "X" + "\033[00m"                # mark hit of the ship in the enemies field colored red
            print("Der Schuss hat" + "\033[31m" + " getroffen!" + "\033[00m")
                                     # c: red                     c: white
            
        elif active_field[shot] == "\033[31m" + "X" + "\033[00m":             # check if field was already shot
            hit = False
            print("Schiffsteil bereits abgeschossen!")

        # check if the shot missed a ship(#)
        elif active_field[shot] != "\033[32m" + "#" + "\33[00m":
            hit = False 
            active_shot_field[shot] = "\033[36m" + "O" + "\033[00m"           # mark corresponding field as a miss(O) colored turquoise
            active_field[shot] = "\033[36m" + "O" + "\033[00m"                # mark miss in the enemies field colored turquoise
            print("Der Schuss ging" + "\033[36m" + " daneben!" + "\033[00m")  # print miss with "daneben" printed blue
                                      # c: blue                  c: white


        #################################################################################################
            # check for victory
        
        ships_left = 0

        # check if a ship-piece(#) is still on the active grid and count up the counter ships_left by one
        for i in range(FIELD_SIZE):
            if active_field[i] == "\033[32m" + "#" + "\33[00m":               
                ships_left += 1                                               
        
        # when counter didn't count up -> no more ship-piece on grid set feedback that one player won and the game shall stop
        if ships_left == 0:                                                   
            victory = 1                                                       


        #################################################################################################
            # switch active player

        # switch to player two to be active when the shot missed
        if hit == False and active_player == 1:         
            active_player = 2
        
        # switch to player one to be active when the shot missed
        elif hit == False and active_player == 2:       
            active_player = 1
        
        
        #################################################################################################
        # check if the player wants to see his own play-field again 

        # if player input is wrong, repeat question again
        wrong_input = True                              
        while wrong_input == True and ships_left != 0:  
            wrong_input = False
            check_self = 0

            try:
                check_self = int(input("Möchtest du dein eigenes Feld noch mal sehen?\n" + "\033[31m" + "0 Nein\n" + "\033[32m" + "1 Ja" + "\33[00m" + "\n"))  
            except ValueError:                                                             # c: red                  # c: green            # c: white
                wrong_input = True  

            # print own field when player demands to see it
            if check_self == 1:
                print("Deine Schiffe:")
                au.print_field(own_field, GRID, FIELD_SIZE)
                check_self = 0
            elif check_self > 1:
                wrong_input = True
                print("Falsche Eingabe (0/1)")
            
        
        input("Beliebige Taste drücken, um fortzufahren")
        print(" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n"" \n")       # create empty space  

        if hit == True and ships_left != 0:
            print(f"Spieler {active_player} hat" + "\033[31m" + " getroffen" + "\033[00m" + " und darf nochmal schießen.")
                                                   # c: red                    c: white


    #####################################################################################################
    '''output victory and winner'''
    #####################################################################################################

    if victory == 1:
        print("Herzlichen Glückwunsch!!! \n" + "\033[1;33m" + "Spieler " + f"{active_player}" + "\033[00m" + " hat" + "\033[32m" + " gewonnen!" + "\33[00m")
                                               # c: yellow                                      c: white              c: green                    c: white    
  
          
    #####################################################################################################
    '''check for end of playing'''
    #####################################################################################################

    wrong_input = True
    while wrong_input == True:
        wrong_input = False
        continue_play = 0

        try:
            continue_play = int(input("Wollen Sie eine weitere Runde spielen?\n" + "\033[31m" + "0 Nein\n" + "\033[32m" + "1 Ja" + "\33[00m" + "\n"))
        except ValueError:                                                         # c: red                  c: green              c: white
            wrong_input = True

        if continue_play > 1:
            wrong_input = True
            print("Falsche Eingabe (0/1)")
        