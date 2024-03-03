def print_field(in_array, GRID):
    ausgabe = "  A B C D E"                                                             # generate the output of fields in terminal
    for i in range(25):

        if (i % GRID) != 0:
            ausgabe = ausgabe + in_array[i] + "|"
        
        else:
            line = int(i / GRID + 1)
            ausgabe = ausgabe + "\n" + str(line) + "|" + in_array[i] + "|"

    print(ausgabe)