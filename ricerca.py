import patterns


# funzione che paragona il pattern con la matrice ed evidenzia gli 1 del pattern
def ricerca(m_piccola, m_grande, m, n):
    daricordare = []
    for jR in range(len(m_piccola) - 1):
        for iR in range(len(m_grande)):
            for iC in range(len(m_grande[0])):
                for jC in range(len(m_piccola[jR])):
                    if m_piccola[jR][jC] == 0:
                        jC += 1
                        break
                    if m_piccola[jR][jC] == 1:
                        if m_grande[iR][iC] == m_piccola[jR][jC]:
                            if (iR, iC) not in daricordare:
                                daricordare.append((iR, iC))
                        else:
                            iC += 1
    data = coloraHQuelliDelPattern(daricordare, m_grande)
    data = coloraVQuelliDelPattern(daricordare, data)

    for i in range(n):
        for j in range(m):
            print(data[i][j], end=" ")
        print()
    print()


# vera funzione evidenzia gli 1 in orizzontale partendo da quelli rimasti in memoria
def coloraHQuelliDelPattern(daricordare, array):
    for i in range(len(daricordare) - 2):
        a = daricordare[i]
        b = daricordare[i + 1]
        c = daricordare[i + 2]
        if b[0] == a[0] and c[0] == a[0]:
            if b[1] == a[1] + 1 and c[1] == a[1] + 2:
                array[a[0]][a[1]] = patterns.colora(1, "COL")
                array[b[0]][b[1]] = patterns.colora(1, "COL")
                array[c[0]][c[1]] = patterns.colora(1, "COL")
            if b[1] != a[1] + 1 or c[1] != a[1] + 2:
                array[a[0]][a[1]] = patterns.colora(1, "OK")
                array[b[0]][b[1]] = patterns.colora(1, "OK")
                array[c[0]][c[1]] = patterns.colora(1, "OK")
    return array


# vera funzione evidenzia gli 1 in verticale partendo da quelli rimasti in memoria
def coloraVQuelliDelPattern(daricordare, array):
    for i in range(len(daricordare)):
        for j in range(len(daricordare)):
            for k in range(len(daricordare)):
                if daricordare[i][0] == daricordare[j][0] - 1 and daricordare[j][0] == daricordare[k][0] - 1:
                    if daricordare[i][1] == daricordare[j][1] and daricordare[j][1] == daricordare[k][1]:
                        array[daricordare[i][0]][daricordare[i][1]] = patterns.colora(1, "COL")
                        array[daricordare[j][0]][daricordare[j][1]] = patterns.colora(1, "COL")
                        array[daricordare[k][0]][daricordare[k][1]] = patterns.colora(1, "COL")
    return array
