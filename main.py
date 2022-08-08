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
    m = 6
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
    print("pattern di ricerca:")
    pattern = patterns.patternI()
    print("\r")

    print("matrice:")
    matrice = matrix()
    print("\r")

    i = 0
    j = 0
    elemento = None
    print("risultato:")
    for i in range(len(matrice)-len(pattern)+1):
        for j in range(len(matrice[i])-len(pattern[i])):
            if pattern[i][j] == matrice[i][j]:
                elemento = patterns.colora(matrice[i][j])
                matrice[i][j]=elemento
                #print(elemento)
                #print("\u001b[00m - posizione ("+str(i)+", "+str(j)+")")
            print(matrice[i][j], end=" ")
        print("\r")



main()