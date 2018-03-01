def scoreRide(car, ride, bonus) :
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
    