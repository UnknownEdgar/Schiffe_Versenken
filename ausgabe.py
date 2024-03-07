def print_field(in_array, GRID, FIELD_SIZE):
    ausgabe = "  A B C D E F G H I J"                                                             # generate the output of fields in terminal
    for i in range(FIELD_SIZE):

        if (i % GRID) != 0:
            ausgabe = ausgabe + in_array[i] + "|"
        
        else:
            line = int(i / GRID + 1)
            ausgabe = ausgabe + "\n" + str(line) + "|" + in_array[i] + "|"

    print(ausgabe)