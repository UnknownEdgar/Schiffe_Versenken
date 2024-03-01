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

# common variables
field_1 = []
field_2 = []
shotfield_1 = []
shotfield_2 = []
victory = False
active_player = 0
shot = False
hit = False

# creating all arrays with SPACES
af.gen_array(field_1, FIELD_SIZE)
af.gen_array(field_2, FIELD_SIZE)
af.gen_array(shotfield_1, FIELD_SIZE)
af.gen_array(shotfield_2, FIELD_SIZE)