import patterns
import ricerca


# creo la matrice in base ai parametri dell'utente partendo da un array di 0 e 1
def matrix(m, n):
    array = [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0]
    matrix = patterns.create(n, m, array)
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
    m = int(input("Quante colonne (valore compreso tra 3 e 6)?"))
    n = int(input("Quante righe (valore compreso tra 3 e 6)? "))
    matrice = matrix(m, n)
    print("\r")

    print("Abbiamo trovato la "+patterns.colora("I", "COL")+" in:")
    ricerca.ricerca(pattern, matrice, m, n)
    return 


main()
