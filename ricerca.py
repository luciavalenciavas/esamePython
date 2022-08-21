import patterns


def ricerca(m_piccola, m_grande, m, n):
    daricordare = []
    for jR in range(len(m_piccola) - 1) :
        for iR in range(len(m_grande)) :
            for iC in range(len(m_grande[0])) :
                for jC in range(len(m_piccola[jR])) :
                    if m_piccola[jR][jC] == 0 :
                        jC += 1
                        break
                    if m_piccola[jR][jC] == 1 :
                        if m_grande[iR][iC] == m_piccola[jR][jC] :
                            if (iR, iC) not in daricordare:
                                daricordare.append((iR, iC))
                        else :
                            iC += 1
    data = coloraHQuelliDelPattern(daricordare, m_grande)
    data = coloraVQuelliDelPattern(daricordare, data)
    #data = coloraVQuelliDelPattern(daricordare, m_grande)

    for i in range(n) :
        for j in range(m) :
            print(data[i][j], end=" ")
        print()
    # return data
    print()
    #print(data)
    print(daricordare)


def coloraHQuelliDelPattern(daricordare, array) :
    for i in range(len(daricordare) - 2) :
        a = daricordare[i]
        b = daricordare[i + 1]
        c = daricordare[i + 2]
        if b[0]==a[0] and c[0]==a[0]:
            if b[1] == a[1] + 1 and c[1] == a[1] + 2 :
                array[a[0]][a[1]] = patterns.colora(1, "COL")
                array[b[0]][b[1]] = patterns.colora(1, "COL")
                array[c[0]][c[1]] = patterns.colora(1, "COL")
            if b[1] != a[1] + 1 or c[1] != a[1] + 2 :
                array[a[0]][a[1]] = patterns.colora(1, "OK")
                array[b[0]][b[1]] = patterns.colora(1, "OK")
                array[c[0]][c[1]] = patterns.colora(1, "OK")
    return array

#da modificare: bisogna prendere gli 1 ma sia della riga successiva(+1) sia di quella ancora dopo(+2)
def coloraVQuelliDelPattern(daricordare, array) :
    for i in range(len(daricordare) - 2) :
        j = i + 1
        #for j in range(7):
        for j in range(len(array[0])+1):
            x = daricordare[i][0]
            if x == daricordare[j][0]:
                j += 1
            if x != daricordare[j][0] :
                if daricordare[i][1] == daricordare[j][1]:
                    array[daricordare[i][0]][daricordare[i][1]]=patterns.colora(1, "COL")
                    array[daricordare[j][0]][daricordare[j][1]] = patterns.colora(1, "COL")
                    j += 1
                    i += 1
    return array