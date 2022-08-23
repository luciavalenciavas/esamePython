# funzione per creare M raggruppamenti di N  dentro una lista
def create(n, m, data):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            if data[j] not in matrix:
                row.append(data[m * i + j])
        matrix.append(row)
    return matrix


# classe per indicare i colori
class bcolors:
    OK = '\u001b[00m'  # bianco
    HIGHLIGHT = '\u001b[36m'  # blu
    RESET = '\033[0m'  # RESET COLOR


# funzione che utilizza la classe BCOLORS per colorare gli elementi in base alla tipologia
def colora(element, come):
    if come == "OK":
        element = bcolors.OK + str(element) + bcolors.RESET
    if come == "COL":
        element = bcolors.HIGHLIGHT + str(element) + bcolors.RESET  # '\u001b[36m1'
    return element


def patternI():
    array = [1, 0, 0, 1, 0, 0, 1, 0, 0]
    pattern = create(3, 3, array)
    for i in range(3):
        for j in range(3):
            if pattern[i][j] == 1:
                col_element = colora(pattern[i][j], "COL")
            else:
                col_element = colora(pattern[i][j], "OK")
            print(col_element, end=" ")
        print()
    return pattern
