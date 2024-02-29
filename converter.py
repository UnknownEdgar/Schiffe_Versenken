def grid_conversion():
    line = int(input("Zeile: "))
    row = int(input("Spalte: "))

    field = row - 1 + ((line - 1) * 5)

    return field