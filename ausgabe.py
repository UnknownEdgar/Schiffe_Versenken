def print_field(in_array):
    ausgabe = "  A B C D E"
    for i in range(25):

        if (i % 5) != 0:
            ausgabe = ausgabe + in_array[i] + "|"
        
        else:
            line = int(i / 5 + 1)
            ausgabe = ausgabe + "\n" + str(line) + "|" + in_array[i] + "|"

    print(ausgabe)