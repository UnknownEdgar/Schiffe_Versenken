def grid_conversion():

    # initialization of the variable for the while loop
    keep_going_r = 0
         
    #################################################################################     
    # while loop for the input of the row with error feedback and conversion to int #
    ################################################################################# 
    while keep_going_r != 1:
        
        keep_going_r = 1
    
        try:
            row = str(input("Spalte: "))
        except ValueError:
            keep_going_r = 0
    
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
            keep_going_r = 0

    # initialization of the variable for the while loop
    keep_going_l = 0

    ############################################################
    # while loop for the input of the line with error feedback #
    ############################################################
    while keep_going_l != 1:

        keep_going_l = 1

        try:
            line = int(input("Zeile: "))
        except ValueError:
            keep_going_l = 0
        
        if 0 < line < 6:
            line = line
        else:
            keep_going_l = 0
            print("Faslche Eingabe (1 - 5)")

    # calculation of the field
    field = i_row + ((line - 1) * 5)

    #return of the field
    return field