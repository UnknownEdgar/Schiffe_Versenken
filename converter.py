def grid_conversion():

    keep_going = 0
    
        
    while keep_going != 1:
        
        keep_going = 1
    
        try:
            row = str(input("Spalte: "))
        except ValueError:
            error = True
    
        if (row == "A") or (row == "a"):
            i_row = 0

        elif (row == "B") or (row == "b"):
            i_row = 1

        elif (row == "C") or (row == "c"):
            i_row = 2

        elif (row == "D") or (row == "d"):
            i_row = 3

        elif (row == "E") or (row == "e"):
            i_row = 4

        else:
            print("Falsche Eingabe (A - E)")
            keep_going = 0

    keep_going = 0

    while keep_going != 1:

        keep_going = 1

        try:
            line = int(input("Zeile: "))
        except ValueError:
            error = True
        
        if 0 < line < 6:
            line = line
        else:
            keep_going = 0
            print("Faslche Eingabe (1 - 5)")


    field = i_row + ((line - 1) * 5)

    return field