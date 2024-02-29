# symbols of the game

#       X = hit
#       O = miss
#       # = ship
#   space = water/placeholder

# common variables
field_1 = []
field_2 = []
shotfield_1 = []
shotfield_2 = []
victory = False
active_player = 0
shot = 0 # shot input by player after grid convertion 
hit = False
player_shot="" # shot input by player 

print("Spieler"+"f{active_player}""ist dran.")
player_shot=input("Auf welches Feld möchten Sie schießen?")

shot=grid_convertion(player_shot)


