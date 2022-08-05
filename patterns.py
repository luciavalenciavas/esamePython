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

# funzione per colorare gli elementi che corrispondono ad 1 e che fanno parte del pattern
def colora(element):
    if element == 1:
        element = '\u001b[36m1'
    elif element == 0:
        element = '\u001b[00m0'
    return element

def patternI():
    array = [1, 0, 0, 1, 0, 0, 1, 0, 0]
    matrix = create(3, 3, array)
    for i in range(3):
        for j in range(3):
            col_element = colora(matrix[i][j])
            print(col_element, end=" ")
        print()
    print('\u001b[00mPattern trovato (simile a una I), ruotato a 0°')


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

#patternI()
#patternL()
#patternC()
#patternT()

