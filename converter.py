#########################################################################################################
#                                       grid-converter
#           converts the line and row inputs of the players in the indexes for the arrays 
#########################################################################################################
def grid_conversion():

    # initialization of the variable for the while loop
    keep_going_r = 0
         
    #####################################################################################################     
    '''while loop for the input of the row with error feedback and conversion to int'''
    ##################################################################################################### 
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

        elif (row == "F") or (row == "f"):
            i_row = 5

        elif (row == "G") or (row == "g"):
            i_row = 6

        elif (row == "H") or (row == "h"):
            i_row = 7

        elif (row == "I") or (row == "i"):
            i_row = 8

        elif (row == "J") or (row == "j"):
            i_row = 9

        else:
            print("Falsche Eingabe (A - J)")
            keep_going_r = 0

    # initialization of the variable for the while loop
    keep_going_l = 0

    #####################################################################################################
    ''''while loop for the input of the line with error feedback'''
    #####################################################################################################
    while keep_going_l != 1:

        keep_going_l = 1
        line = 0
        try:
            line = int(input("Zeile: "))
        except ValueError:
            keep_going_l = 0
        
        if 0 < line < 11:
            line = line
        else:
            keep_going_l = 0
            print("Falsche Eingabe (1 - 10)")

    # calculation of the field
    field = i_row + ((line - 1) * 10)

    #return of the field
    return field