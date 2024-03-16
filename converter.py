#########################################################################################################
#                                       grid-converter
#           converts the line and row inputs of the players in the indexes for the arrays 
#########################################################################################################




#########################################################################################################
#                                           Function 
#########################################################################################################

def grid_conversion(GRID):
       
    #####################################################################################################     
    '''while loop for the input of the row with error feedback and conversion to int'''
    ##################################################################################################### 
    
    # initialization of the variable for the while loop
    wrong_input = True
    
    while wrong_input == True:
        
        wrong_input = False
    
        try:
            row = str(input("Spalte: "))
        except ValueError:
            wrong_input = True
    
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
            wrong_input = True

    #####################################################################################################
    ''''while loop for the input of the line with error feedback'''
    #####################################################################################################
    
     # initialization of the variable for the while loop
    wrong_input = True
    
    while wrong_input == True:

        wrong_input = False
        line = 0
        try:
            line = int(input("Zeile: "))
        except ValueError:
            wrong_input = True
        
        if 0 < line < 11:
            line = line
        else:
            wrong_input = True
            print("Falsche Eingabe (1 - 10)")

    # calculation of the field
    field = i_row + ((line - 1) * GRID)

    # return of the field
    return field