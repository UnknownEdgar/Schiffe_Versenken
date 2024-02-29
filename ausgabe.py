def print_field(in_array):
    for i in range(25):
        if (i % 5) != 0:
            ausgabe = in_array[i]
        else:
            ausgabe = "\n" + in_array[i]