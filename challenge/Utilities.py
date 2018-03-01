import random as rd

def distance(ride):
    return abs(ride['pos_finish'][0] - ride['pos_start'][0]) + abs(ride['pos_finish'][1] - ride['pos_start'][1])

def setTimer(voiture, ride, currentTime, tableauCar, tableauRide):
    car = posCar(voiture, tableauCar, tableauRide)
    tempsTrajet = abs(car[0] - ride['pos_start'][0]) + abs(car[1] - ride['pos_start'][1])
    tempsAttente = max(0, ride['start'] - (tempsTrajet + currentTime))
    return distance(ride) + tempsAttente + tempsTrajet

def DetectZero(TableauTimer):
    res = []
    for i in range(len(TableauTimer)):
        if TableauTimer[i] == 0:
            res.append(i)
    return res

def TempsSuivant(TableauTimer):
    for x in TableauTimer:
        x -= 1

def posCar(nCar, tableauCar, tableauRide):
    length = len(tableauCar[nCar])
    if length == 0:
        return (0, 0)
    return (tableauRide[tableauCar[-1]]['pos_finish'][0], tableauRide[tableauCar[-1]]['pos_finish'][1])

def modify(ride_assignement) :
    N = len(ride_assignement)
    a = rd.randint(0,N-1)
    b = rd.randint(0,N-1)
    x = rd.randint(0,len(ride_assignement[a])-1)
    y = rd.randint(0,len(ride_assignement[b])-1)
    temp = ride_assignement[a][x]
    ride_assignement[a][x] = ride_assignement[b][y]
    ride_assignement[b][y] = temp