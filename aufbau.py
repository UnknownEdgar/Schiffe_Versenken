# import of all requiered modules/files
import ausgabe as a
import converter as cv

# function generating placement of the ships
def aufbau(field_player, FIELD_SIZE, GRID):
      
      a.print_field(field_player, GRID, FIELD_SIZE)

      print("In welche Felder möchtest du deine Schiffe setzen?\nZur Verfügung stehen 1 Schlachtschiff (5 Felder), 2 Kreuzer (4 Felder), 3 Zerstörer (3 Felder), 4 U-Boote (2 Felder).\nDie Schiffe werden auch in dieser Reihenfolge (5 -> 2) platziert.\nBitte gib immer das linke obere Feld an.")
    
      ship = 0

      # loop placement of all 10 ships
      while ship < 10 :
      
            field = cv.grid_conversion()

            try:
                  dir = int(input("Soll das Schiff horizontal (0) oder vertikal (1) stehen?\nMit 8 kann das Spielfeld zurückgesetzt werden\n"))
            except ValueError:
                  error = True

            # placement of ships with size of 5
            if dir == 8:
                  
                  # empty the field while placement
                  
                  gen_empty(field_player, FIELD_SIZE)
                  ship = 0

            else:

                  if ship < 1:
                        
                        SHIP_SIZE = 5
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)
                  
                  # placement of ships with size of 2
                  elif 1 <= ship < 3:

                        SHIP_SIZE = 4
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)

                  elif 3 <= ship < 6:

                        SHIP_SIZE = 3
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)

                  elif 6 <= ship < 10:

                        SHIP_SIZE = 2
                        ship = place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, dir, ship)        


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

# functions to generate the supporting characters among the rules of the game
def add_left(field_array, pos, grid):
      if (pos % grid) > 0:
            field_array[pos - 1] = "\033[1;30m" + "O" + "\033[00m"

def add_right(field_array, pos, grid):
      if (pos % grid) < 4:
            field_array[pos + 1] = "\033[1;30m" + "O" + "\033[00m"

def add_above(field_array, pos, grid):
      if pos > (grid - 1):
            field_array[pos - grid] = "\033[1;30m" + "O" + "\033[00m"

def add_below(field_array, pos, field_size, grid):
      if pos < (field_size - grid):
            field_array[pos + grid] = "\033[1;30m" + "O" + "\033[00m"

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

def place_ship(field, field_player, FIELD_SIZE, SHIP_SIZE, GRID, direction, ship):
      
      error_hor = False
      error_ver = False

      for i in range(SHIP_SIZE):
            
            if dir == 0 and  field > (FIELD_SIZE - SHIP_SIZE):
                  error_hor = True
            
            elif dir == 0 and (field_player[field + i] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + i] == "\033[32m" + "#" + "\33[00m" or (field % GRID) > (GRID - SHIP_SIZE)):
                  error_hor = True
   
      for i in range(SHIP_SIZE):

            if dir == 1 and field >= (FIELD_SIZE - ((SHIP_SIZE - 1) * GRID)):
                  error_ver = True
            
            elif dir == 1 and (field_player[field + (i * GRID)] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + (i * GRID)] == "\033[32m" + "#" + "\33[00m"):
                  error_ver = True

      # horizontal placement of ship
      if direction == 0 and (field % GRID) < (GRID - SHIP_SIZE + 1) and error_hor == False:                        
            ship += 1
            add_left(field_player, field, GRID)
            for i in range(SHIP_SIZE):
                  field_player[field + i] = "\033[32m" + "#" + "\33[00m"
                  add_abr(field_player, field, i, FIELD_SIZE, GRID)
      
      # vertical placement of ship
      elif dir == 1 and error_ver == False:
            ship += 1
            add_above(field_player, field, GRID)
            for i in range(SHIP_SIZE):
                  field_player[field + (i * GRID)] = "\033[32m" + "#" + "\33[00m"
                  add_blr(field_player, field, (i * GRID), FIELD_SIZE, GRID)

      else:
            print("Falsche Eingabe. Bitte erneut probieren")

      return ship