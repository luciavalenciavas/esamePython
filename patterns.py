# funzione per creare la matrice con MxN caselle in base agli elementi di una lista
def create(n, m, data):
    matrix = []
    for i in range(n): #n=rows number
        row = []
        for j in range(m): #m=columns number
            if data[j] not in matrix:
                row.append(data[m * i + j])
        matrix.append(row)
    return matrix


class bcolors:
    OK = '\u001b[00m' #bianco
    HIGHLIGHT = '\u001b[36m' #blu
    RESET = '\033[0m'  # RESET COLOR

# funzione per colorare gli elementi che corrispondono ad 1 e che fanno parte del pattern
def colora(element,come):
    if come == "OK":
        element = bcolors.OK + str(element) + bcolors.RESET
    if come=="COL":
        element = bcolors.HIGHLIGHT + str(element) + bcolors.RESET  # '\u001b[36m1'
    return element


def patternI():
    array = [1, 0, 0, 1, 0, 0, 1, 0, 0]
    pattern = create(3, 3, array)
    for i in range(3):
        for j in range(3):
            #col_element = colora(pattern[i][j])
            if pattern[i][j] == 1:
                col_element = colora(pattern[i][j], "COL")
            else:
                col_element = colora(pattern[i][j], "OK")
            print(col_element, end=" ")
            # print(pattern[i][j], end=" ")
        print()
    return pattern
    # print('\u001b[00mPattern trovato (simile a una I), ruotato a 0°')


# def patternL():
#     array = [1, 0, 0, 1, 0, 0, 1, 1, 1]
#     matrix = create(3, 3, array)
#     for i in range(3):
#      for j in range(3):
#          col_element = colora(matrix[i][j])
#          print(col_element, end=" ")
#      print()
#     print('\u001b[00mPattern trovato (simile a una L), ruotato a 0°')
#
#
# def patternC():
#     array = [1, 1, 1, 1, 0, 0, 1, 1, 1]
#     matrix = create(3, 3, array)
#     for i in range(3):
#      for j in range(3):
#          col_element = colora(matrix[i][j])
#          print(col_element, end=" ")
#      print()
#     print('\u001b[00mPattern trovato (simile a una C), ruotato a 0°')
#
#
# def patternT():
#     array = [1, 1, 1, 0, 1, 0, 0, 1, 0]
#     matrix = create(3, 3, array)
#     for i in range(3):
#      for j in range(3):
#          col_element = colora(matrix[i][j])
#          print(col_element, end=" ")
#      print()
#     print('\u001b[00mPattern trovato (simile a una T), ruotato a 0°')

# patternI()
# patternL()
# patternC()
# patternT()

