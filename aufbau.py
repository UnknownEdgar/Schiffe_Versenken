import ausgabe as a
import converter as cv
def aufbau(field_player):
    a.print_field(field_player)

    print("In welche Felder möchtest du deine Schiffe setzen?\n"
          "Zur Verfügung stehen 2 Schiffe mit 3 Feldern und 2 Schiffe mit 2 Feldern\n"
          "Bitte gib das linke obere Feld an.")
    
    ship = 0

    while ship < 4 :
      
      field = cv.grid_conversion()

      dir = int(input("Soll das Schiff horizontal (0) oder vertikal (1) stehen? "))

      if ship < 2:
            
            if dir == 0 and (field % 5) < 3:
                  ship += 1
                  add_left(field_player, field)
                  for i in range(3):
                        field_player[field + i] = "#"
                        add_abr(field_player, field + i)

            elif dir == 1 and field < 15:
                  ship += 1
                  add_above(field_player, field)
                  for i in range(3):
                        field_player[field + (i * 5)] = "#"
                        add_blr(field_player, field, (i * 5))

            else:
                print("Falsche Eingabe. Bitte erneut probieren")
      
      elif 2 <= ship < 4:
            
            if dir == 0 and (field % 5) < 4:
                  ship += 1
                  add_left(field_player, field)
                  for i in range(2):
                       field_player[field + i] = "#"
                       add_abr(field_player, field + i)
            
            elif dir == 1 and field < 20:
                  ship +=1
                  add_above(field_player, field)
                  for i in range(2):
                       field_player[field + (i * 5)] = "#"
                       add_blr(field_player, field, (i * 5))
            
            else:
                print("Falsche Eingabe. Bitte erneut probieren")

      else:
            for i in range(25):
                  if field_player[i] == "O":
                        field_player[i] = " "

                  else:
                       field_player[i] = field_player[i]                  

      print("Aktuelles Spielfeld")
      a.print_field(field_player)

def add_left(field_array, pos):
      if (pos % 5) > 0:
            field_array[pos - 1] = "O"

def add_right(field_array, pos):
      if (pos % 5) < 4:
            field_array[pos + 1] = "O"

def add_above(field_array, pos):
      if pos > 4:
            field_array[pos - 5] = "O"

def add_below(field_array, pos):
      if pos < 20:
            field_array[pos + 5] = "O"

def add_abr(playfield, position, loop):
      add_above(playfield, position + loop)
      add_below(playfield, position + loop)
      add_right(playfield, position + loop)

def add_blr(playfield, position, loop):
      add_below(playfield, position + loop)
      add_left(playfield, position + loop)
      add_right(playfield, position + loop)