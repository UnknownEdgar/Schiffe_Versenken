# import of all requiered modules/files
import ausgabe as a
import converter as cv

# function generating placement of the ships
def aufbau(field_player, FIELD_SIZE, GRID):
      
      a.print_field(field_player, GRID, FIELD_SIZE)   # print the playfield

      print("In welche Felder möchtest du deine Schiffe setzen?\nZur Verfügung stehen 1 Schlachtschiff (5 Felder), 2 Kreuzer (4 Felder), 3 Zerstörer (3 Felder), 4 U-Boote (2 Felder).\nDie Schiffe werden auch in dieser Reihenfolge (5 -> 2) platziert.\nBitte gib immer das linke obere Feld an.")
    
      ship = 0

      # loop placement of all 10 ships
      while ship < 10 :
      
            which_ship(ship)

            field = cv.grid_conversion()

            try:
                  dir = int(input("Soll das Schiff horizontal (0) oder vertikal (1) stehen?\nMit 8 kann das Spielfeld zurückgesetzt werden\n"))
            except ValueError:
                  error = True

            # check if the user wants to reset the board
            if dir == 8:
                  
                  # empty the field and restart the process to place the ships
                  gen_empty(field_player, FIELD_SIZE)
                  ship = 0

            # continue if no reset was chosen
            else:

                  # place the ship with size 5
                  if ship < 1:
                        
                        SHIP_SIZE = 5
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)
                  
                  # placement of the ships with size 4
                  elif 1 <= ship < 3:

                        SHIP_SIZE = 4
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)

                  # placement of the ships with size 3
                  elif 3 <= ship < 6:

                        SHIP_SIZE = 3
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)

                  # placement of the ships with size 2
                  elif 6 <= ship < 10:

                        SHIP_SIZE = 2
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)        


            # print the current field after placing the ship
            a.print_field(field_player, GRID, FIELD_SIZE)

      # delete support characters for ship placement
      for i in range(FIELD_SIZE):
            if field_player[i] == "\033[1;30m" + "O" + "\033[00m":
                  field_player[i] = " "

            else:
                  field_player[i] = field_player[i]           
      
      # show the field with placed ships
      print("Aktuelles Spielfeld")
      a.print_field(field_player, GRID, FIELD_SIZE)

# functions to generate the supporting characters to comply to the rules of the game
def add_left(field_array, pos, grid):
      if (pos % grid) > 0:
            field_array[pos - 1] = "\033[1;30m" + "O" + "\033[00m"

def add_right(field_array, pos, grid):
      if (pos % grid) < (grid - 1):
            field_array[pos + 1] = "\033[1;30m" + "O" + "\033[00m"

def add_above(field_array, pos, grid):
      if pos > (grid - 1):
            field_array[pos - grid] = "\033[1;30m" + "O" + "\033[00m"

def add_below(field_array, pos, field_size, grid):
      if pos < (field_size - grid):
            field_array[pos + grid] = "\033[1;30m" + "O" + "\033[00m"

# combination of some functions of the generation of support characters
def add_abr(playfield, position, loop, field_size, grid):
      add_above(playfield, position + loop, grid)
      add_below(playfield, position + loop, field_size, grid)
      add_right(playfield, position + loop, grid)

def add_blr(playfield, position, loop, field_size, grid):
      add_below(playfield, position + loop, field_size, grid)
      add_left(playfield, position + loop, grid)
      add_right(playfield, position + loop, grid)

# function to empty the field
def gen_empty(field_array, field_size):
      for i in range(field_size):
            field_array[i] = " "

# funtion to genrate the field
def gen_array(in_array,size):
      for i in range(size):
            in_array.append(" ")

# function to place the ships on the playfield
def place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, direction, ship):
      
      # initialize the error variables
      error_hor = False
      error_ver = False

      # the ships aren't allowed to be placed in a field where
            #     - the ship would exceed the maximum number of rows
            #     - the ship would exceed the maximum number of lines
            #     - a support character or boat is placed
      
      # check for horizontal placement error
      for i in range(SHIP_SIZE):
            
            if direction == 0 and  field > (FIELD_SIZE - SHIP_SIZE):
                  error_hor = True
            
            elif direction == 0 and (field_player[field + i] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + i] == "\033[32m" + "#" + "\33[00m" or (field % GRID) > (GRID - SHIP_SIZE)):
                  error_hor = True
      
      # check for vertical placement error
      for i in range(SHIP_SIZE):

            if direction == 1 and field >= (FIELD_SIZE - ((SHIP_SIZE - 1) * GRID)):
                  error_ver = True
            
            elif direction == 1 and (field_player[field + (i * GRID)] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + (i * GRID)] == "\033[32m" + "#" + "\33[00m"):
                  error_ver = True

      # placement of the ships
      #     add a boat character to every field where it should be
      #     add support characters to all surrounding fields

      # horizontal placement of ship
      if direction == 0 and (field % GRID) < (GRID - SHIP_SIZE + 1) and error_hor == False:                        
            ship += 1
            add_left(field_player, field, GRID)
            for i in range(SHIP_SIZE):
                  field_player[field + i] = "\033[32m" + "#" + "\33[00m"
                  add_abr(field_player, field, i, FIELD_SIZE, GRID)
      
      # vertical placement of ship
      elif direction == 1 and error_ver == False:
            ship += 1
            add_above(field_player, field, GRID)
            for i in range(SHIP_SIZE):
                  field_player[field + (i * GRID)] = "\033[32m" + "#" + "\33[00m"
                  add_blr(field_player, field, (i * GRID), FIELD_SIZE, GRID)

      else:
            print("Falsche Eingabe. Bitte erneut probieren")

      # return the integer ship to get to the next ship or repeat the process with the same ship
      return ship

# show the user which ship is to be placed
def which_ship(ship):
      if ship == 0:
            print("Platziere bitte dein Schiff der Größe 5")
      elif 1 <= ship < 3:
            print("Platziere bitte dein Schiff der Größe 4")
      elif 3 <= ship < 6:
            print("Platziere bitte dein Schiff der Größe 3")
      elif 6 <= ship < 10:
            print("Platziere bitte dein Schiff der Größe 2")