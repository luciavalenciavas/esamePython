import patterns
import ricerca

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
def matrix(m, n):
    #m = int(input("Quante colonne (massimo 6)?"))
    #n = int(input("Quante righe (massimo 6)? "))
    #m = 5
    #n = 5
    array = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    matrix = patterns.create(n, m, array)
    #print (len(array))
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
    m = int(input("Quante colonne (massimo 6)?"))
    n = int(input("Quante righe (massimo 6)? "))
    matrice = matrix(m, n)
    print("\r")

    print("risultato: Abbiamo trovato la I in:")
    newArray = ricerca.ricerca(pattern, matrice, m, n)
    return 


main()