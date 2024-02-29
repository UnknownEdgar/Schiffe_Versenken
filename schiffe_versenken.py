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


if active_player == 1:      #Check which player is active and assign 
    active_field=field_2    # the corresponding fields to be active
    active_shot_field=shotfield_1
elif active_player == 2:
    active_field=field_1
    active_shot_field=shotfield_2


print("Spieler"+"f{active_player}""ist dran.")
player_shot=input("Auf welches Feld möchten Sie schießen?")


print_field(active_shot_field)


shot=grid_convertion(player_shot)




