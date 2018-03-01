def scoreRide(car, ride, time, bonus, tableauCar, tableauRide) :
    (xCar, yCar) = posCar(car, tableauCar, tableauRide):
    xStart = ride['pos_start'][0]
    yStart = ride['pos_start'][1]
    xFinish = ride['pos_finish'][0]
    yFinish = ride['pos_finish'][1]
    timeArriving = abs(xCar-xStart) + abs(yCar-yStart)
    timeRide = abs(xFinish-xStart) + abs(yFinish-yStart)
    totalTime = timeArriving + timeRide
    if (time + totalTime) > ride[3] :
        return 0
    elif (time + timeArriving) <= ride[2] :
        return timeRide + bonus
    else :
        return timeRide

def totalScore(schedule, bonus) :
    score = 0
    for i in schedule :
        score = score + chainScore(i, bonus)
    return score

def chainScore(carSchedule, bonus) :
    time = 0
    score = 0
    car = [0,0]
    for ride in carSchedule :
        score = score + scoreRide(car, ride, time, bonus)
        xStart = ride['pos_start'][0]
        yStart = ride['pos_start'][1]
        xFinish = ride['pos_finish'][0]
        yFinish = ride['pos_finish'][1]
        timeArriving = abs(xCar-xStart) + abs(yCar-yStart)
        timeRide = abs(xFinish-xStart) + abs(yFinish-yStart)
        totalTime = timeArriving + timeRide
        car = [xFinish, yFinish]
        time = max(ride[2] + timeRide, time + totalTime)
    return score
