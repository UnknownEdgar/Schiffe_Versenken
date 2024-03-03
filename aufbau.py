import ausgabe as a
import converter as cv
def aufbau(field_player, FIELD_SIZE, GRID):
      
      a.print_field(field_player)

      print("In welche Felder möchtest du deine Schiffe setzen?\nZur Verfügung stehen 2 Schiffe mit 3 Feldern und 2 Schiffe mit 2 Feldern\nBitte gib das linke obere Feld an.")
    
      ship = 0

      while ship < 4 :
      
            field = cv.grid_conversion()

            try:
                  dir = int(input("Soll das Schiff horizontal (0) oder vertikal (1) stehen?\nMit 8 kann das Spielfeld zurückgesetzt werden\n"))
            except ValueError:
                  error = True

            error_hor = False
            error_ver = False

            if ship < 2 and dir != 8:
                  
                  SHIP_SIZE = 3

                  for i in range(SHIP_SIZE):
                              if dir == 0 and  field > (FIELD_SIZE - SHIP_SIZE):
                                    error_hor = True
                              elif dir == 0 and (field_player[field + i] == "O" or field_player[field + i] == "X" or (field % GRID) > (GRID - SHIP_SIZE)):
                                    error_hor = True
                              if dir == 1 and field >= (FIELD_SIZE - ((SHIP_SIZE - 1) * GRID)):
                                    error_ver = True
                              elif dir == 1 and (field_player[field + (i * GRID)] == "O" or field_player[field + i] == "X"):
                                    error_ver = True

                  if dir == 0 and (field % GRID) < (GRID - SHIP_SIZE + 1) and error_hor == False:                        
                        ship += 1
                        add_left(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + i] = "#"
                              add_abr(field_player, field, i, FIELD_SIZE, GRID)

                  elif dir == 1 and error_ver == False:
                        ship += 1
                        add_above(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + (i * GRID)] = "#"
                              add_blr(field_player, field, (i * GRID), FIELD_SIZE, GRID)

                  else:
                        print("Falsche Eingabe. Bitte erneut probieren")
            
            elif 2 <= ship < 4 and dir != 8:

                  SHIP_SIZE = 2

                  for i in range(SHIP_SIZE):
                        if dir == 0 and  field > (FIELD_SIZE - SHIP_SIZE):
                              error_hor = True
                        elif dir == 0 and (field_player[field + i] == "O" or field_player[field + i] == "X") or (field % GRID) > (GRID - SHIP_SIZE):
                              error_hor = True
                        if dir == 1 and field >= (FIELD_SIZE - ((SHIP_SIZE - 1) * GRID)):
                              error_ver = True
                        elif dir == 1 and (field_player[field + (i * GRID)] == "O" or field_player[field + i] == "X"):
                              error_ver = True
                  
                  if dir == 0 and error_hor == False:
                        ship += 1
                        add_left(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + i] = "#"
                              add_abr(field_player, field, i, FIELD_SIZE, GRID)
                  
                  elif dir == 1 and error_ver == False:
                        ship += 1
                        add_above(field_player, field, GRID)
                        for i in range(SHIP_SIZE):
                              field_player[field + (i * GRID)] = "#"
                              add_blr(field_player, field, (i * GRID), FIELD_SIZE, GRID)
                  
                  else:
                        print("Falsche Eingabe. Bitte erneut probieren")
            
            elif dir == 8:
                  gen_empty(field_player, FIELD_SIZE)
                  ship = 0

            a.print_field(field_player)

      for i in range(FIELD_SIZE):
            if field_player[i] == "O":
                  field_player[i] = " "

            else:
                  field_player[i] = field_player[i]           

      print("Aktuelles Spielfeld")
      a.print_field(field_player)

def add_left(field_array, pos, grid):
      if (pos % grid) > 0:
            field_array[pos - 1] = "O"

def add_right(field_array, pos, grid):
      if (pos % grid) < 4:
            field_array[pos + 1] = "O"

def add_above(field_array, pos, grid):
      if pos > (grid - 1):
            field_array[pos - grid] = "O"

def add_below(field_array, pos, field_size, grid):
      if pos < (field_size - grid):
            field_array[pos + grid] = "O"

def add_abr(playfield, position, loop, field_size, grid):
      add_above(playfield, position + loop, grid)
      add_below(playfield, position + loop, field_size, grid)
      add_right(playfield, position + loop, grid)

def add_blr(playfield, position, loop, field_size, grid):
      add_below(playfield, position + loop, field_size, grid)
      add_left(playfield, position + loop, grid)
      add_right(playfield, position + loop, grid)

def gen_empty(field_array, field_size):
      for i in range(field_size):
            field_array[i] = " "

def gen_array(in_array,size):
      for i in range(size):
            in_array.append(" ")