def ricerca(m_piccola, m_grande):
    iR = 0
    jR = 0
    obj = []
    while iR < len(m_grande):
        while jR < len(m_piccola):
            iC = 0
            jC = 0
            while iC < len(m_grande[0]):
                while jC < len(m_piccola[jR]):
                    indice_c_piccola = jC
                    if m_grande[iR][iC] == m_piccola[jR][indice_c_piccola] and m_piccola[jR][indice_c_piccola] == 1:
                        obj.append(m_grande[iR][iC])
                        print("\u001b[36m" + str(m_grande[iR][iC]), end=" ")
                    else:
                        print("\u001b[00m" + str(m_grande[iR][iC]), end=" ")
                    jC += 1
                    if jC == len(m_piccola[jR]):
                        jC = 0
                    iC += 1
                    if iC == len(m_grande[jR]):
                        print()
                        break
            jR += 1
            if jR == len(m_piccola):
                jR = 0
            iR += 1
            if iR == len(m_grande):
                break
    print("obj (ossia gli uno che ha trovato)", obj)

