def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def coutTrajet(xVoiture, yVoiture, xDepart, yDepart, xArrivee, yArrivee):
    return distance(xVoiture, yVoiture, xDepart, yDepart) + distance(xDepart, yDepart, xArrivee, yArrivee)
