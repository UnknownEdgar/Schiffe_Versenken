# import of all requiered modules/files
import ausgabe as a
import converter as cv

# function generating placement of the ships
def aufbau(field_player, FIELD_SIZE, GRID):
      
      a.print_field(field_player, GRID)

      print("In welche Felder möchtest du deine Schiffe setzen?\nZur Verfügung stehen 2 Schiffe mit 3 Feldern und 2 Schiffe mit 2 Feldern.\nDie Schiffe werden auch in dieser Reihenfolge (3 -> 2) platziert.\nBitte gib das linke obere Feld an.")
    
      ship = 0

      # loop placement of all 4 ships
      while ship < 4 :
      
            field = cv.grid_conversion()

            try:
                  dir = int(input("Soll das Schiff horizontal (0) oder vertikal (1) stehen?\nMit 8 kann das Spielfeld zurückgesetzt werden\n"))
            except ValueError:
                  error = True

            error_hor = False
            error_ver = False

            # placement of ships with size of 3
            if ship < 2 and dir != 8:
                  
                  SHIP_SIZE = 3

                  for i in range(SHIP_SIZE):
                              
                              # check for errors in horizontal placement
                              if dir == 0 and  field > (FIELD_SIZE - SHIP_SIZE):
                                    error_hor = True
                              elif dir == 0 and (field_player[field + i] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + i] == "\033[32m" + "#" + "\33[00m" or (field % GRID) > (GRID - SHIP_SIZE)):
                                    error_hor = True

                              # check for errors in vertical placement
                              if dir == 1 and field >= (FIELD_SIZE - ((SHIP_SIZE - 1) * GRID)):
                                    error_ver = True
                              elif dir == 1 and (field_player[field + (i * GRID)] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + i] == "\033[32m" + "#" + "\33[00m"):
                                    error_ver = True

                  # horizontal placement of ship with size 3
                  if dir == 0 and (field % GRID) < (GRID - SHIP_SIZE + 1) and error_hor == False:                        
                        ship += 1
                        add_left(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + i] = "\033[32m" + "#" + "\33[00m"
                              add_abr(field_player, field, i, FIELD_SIZE, GRID)

                  # vertical placement of ship with size 3
                  elif dir == 1 and error_ver == False:
                        ship += 1
                        add_above(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + (i * GRID)] = "\033[32m" + "#" + "\33[00m"
                              add_blr(field_player, field, (i * GRID), FIELD_SIZE, GRID)

                  else:
                        print("Falsche Eingabe. Bitte erneut probieren")
            
            # placement of ships with size of 2
            elif 2 <= ship < 4 and dir != 8:

                  SHIP_SIZE = 2

                  for i in range(SHIP_SIZE):

                        # check for errors in horizontal placement
                        if dir == 0 and  field > (FIELD_SIZE - SHIP_SIZE):
                              error_hor = True
                        elif dir == 0 and (field_player[field + i] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + i] == "\033[32m" + "#" + "\33[00m") or (field % GRID) > (GRID - SHIP_SIZE):
                              error_hor = True

                        # check for errors in vertical placement
                        if dir == 1 and field >= (FIELD_SIZE - ((SHIP_SIZE - 1) * GRID)):
                              error_ver = True
                        elif dir == 1 and (field_player[field + (i * GRID)] == "\033[1;30m" + "O" + "\033[00m" or field_player[field + i] == "\033[32m" + "#" + "\33[00m"):
                              error_ver = True
                  
                  # horizontal placement of ship with size 2
                  if dir == 0 and error_hor == False:
                        ship += 1
                        add_left(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + i] = "\033[32m" + "#" + "\33[00m"
                              add_abr(field_player, field, i, FIELD_SIZE, GRID)
                  
                  # vertical placement of ship with size 2
                  elif dir == 1 and error_ver == False:
                        ship += 1
                        add_above(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + (i * GRID)] = "\033[32m" + "#" + "\33[00m"
                              add_blr(field_player, field, (i * GRID), FIELD_SIZE, GRID)
                  
                  else:
                        print("Falsche Eingabe. Bitte erneut probieren")
            
            # empty the field while placement
            elif dir == 8:
                  gen_empty(field_player, FIELD_SIZE)
                  ship = 0

            a.print_field(field_player, GRID)

      # delete support characters for ship placement
      for i in range(FIELD_SIZE):
            if field_player[i] == "\033[1;30m" + "O" + "\033[00m":
                  field_player[i] = " "

            else:
                  field_player[i] = field_player[i]           
      # show the field with placed ships
      print("Aktuelles Spielfeld")
      a.print_field(field_player, GRID)

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