def creationPart(tableau, R, C, L, H):
    i = 0
    j = 0
    while !valide(tableau, debut, fin):
        j = j+1



def valide(tableau, debut, fin):
    first = tableau[debut][0]
    for i in range(debut, fin + 1):
        for j in range(C):
            if tableau[i][j] != first:
                return True
    return False
