def scoreRide(car, ride, time, bonus) :
    xCar = car[0]
    yCar = car[1]
    xStart = ride[0][0]
    yStart = ride[0][1]
    xFinish = ride[1][0]
    yFinish = ride[1][1]
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
        xStart = ride[0][0]
        yStart = ride[0][1]
        xFinish = ride[1][0]
        yFinish = ride[1][1]
        timeArriving = abs(xCar-xStart) + abs(yCar-yStart)
        timeRide = abs(xFinish-xStart) + abs(yFinish-yStart)
        totalTime = timeArriving + timeRide
        car = [xFinish, yFinish]
        time = max(ride[2] + timeRide, time + totalTime)
    return score