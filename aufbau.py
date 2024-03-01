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

      dir = int(input("Soll das Schiff vertikal (0) oder horizontal (1) stehen? "))

      if ship < 2:
            
            if dir == 0 and (field % 5) < 3:
                  ship += 1
                  for i in range(3):
                     field_player[field + i] = "#"

            elif dir == 1 and field < 15:
                  ship += 1
                  for i in range(3):
                    field_player[field + (i * 5)] = "#"

            else:
                print("Falsche Eingabe. Bitte erneut probieren")
      
      else:
            
            if dir == 0 and (field % 5) < 4:
                  ship += 1
                  for i in range(2):
                       field_player[field + i] = "#"
            
            elif dir == 1 and field < 20:
                  
                  ship +=1
                  for i in range(2):
                       field_player[field + (i * 5)] = "#"

      print("Aktuelles Spielfeld")
      a.print_field(field_player)      