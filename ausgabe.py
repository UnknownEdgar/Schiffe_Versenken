# function to create the grid as a string to output on the command line
def print_field(in_array, GRID, FIELD_SIZE):
    
    # start the string with the letters for the rows
    ausgabe = "   A B C D E F G H I J"                                                             # generate the output of fields in terminal
    
    # loop to add all numbers, lines and ships to the string
    for i in range(FIELD_SIZE):

        # add only "|" in between the fields
        if (i % GRID) != 0:
            ausgabe = ausgabe + in_array[i] + "|"
        
        # add the line break, add the "space" to get an even grid layout and add the line number
        elif i < (FIELD_SIZE - GRID -  1):
            line = int(i / GRID + 1)
            ausgabe = ausgabe + "\n " + str(line) + "|" + in_array[i] + "|"

        # add the last line without the "space"
        else:
            line = int(i / GRID + 1)
            ausgabe = ausgabe + "\n" + str(line) + "|" + in_array[i] + "|"

    # print the grid to the command line
    print(ausgabe)