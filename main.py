import patterns


# def create(n, m, data):
#     matrix = []
#     for i in range(n): #n=rows number
#         row = []
#         for j in range(m): #m=columns number
#             if data[j] not in matrix:
#                 row.append(data[m * i + j])
#         matrix.append(row)
#     return matrix




# imposto la lista, creo la matrice e stampo le righe una sotto l'altra
def matrix():
    #m = int(input("How many columns?"))
    #n = int(input("How many rows?"))
    m = 5
    n = 5
    array = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    matrix = patterns.create(n, m, array)
    #print(matrix)
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()
    return matrix



def main():
    pattern = patterns.patternI()
    matrice = matrix()
    if pattern in matrice:
        print("c'è")
    else:
        print("non c'è")


main()