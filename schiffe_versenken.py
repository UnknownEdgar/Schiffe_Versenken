# symbols of the game

#       X = hit
#       O = miss
#       # = ship
#   space = water/placeholder

# common variables
active_field = []
active_shot_field=[]
field_1 = []
field_2 = []
shotfield_1 = []
shotfield_2 = []
victory = False
active_player = 0
shot = 0 # shot input by player after grid convertion 
hit = False
player_shot="" # shot input by player 


####################################################################
    #active player check

if active_player == 1:      #Check which player is active and assign 
    active_field=field_2    # the corresponding fields to be active
    active_shot_field=shotfield_1
elif active_player == 2:
    active_field=field_1
    active_shot_field=shotfield_2

####################################################################
    #shot input and convertion

print("Spieler "+"f{active_player}"" ist dran.")
player_shot=input("Auf welches Feld möchten Sie schießen?")


print_field(active_shot_field)


shot=grid_convertion(player_shot)

#####################################################################
    # hit detection

if active_field[shot]== "#":        #Check if the shot hit a ship(#)
    hit=True                        
    active_shot_field[shot]="X"     # mark corresponding field as a hit(X)
    active_field[shot]=" "          # delete the ship in the enemies field
    print("Der Schuss hat getroffen!")

elif active_field[shot] != "#":     #Check if the shot missed a ship(#)
    hit=False
    active_shot_field[shot]="O"     # mark corresponding field as a miss(O)
    print("Der Schuss ging daneben!")

#######################################################################
    #Check for victory


########################################################################
    # Switch active player

if hit== False and active_player==1:
    active_player=2

if hit== False and active_player==2:
    active_player=1












