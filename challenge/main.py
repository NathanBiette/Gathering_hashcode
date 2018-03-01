from gathering_parser import GatheringParser as Parser
import sys
from math import *
import random
from Utilities.py import *

parser = Parser()
if len(sys.argv) == 2:
    info = parser.parse(sys.argv[1])
    print(info)
else:
    print("Syntax error:\r\nUsage : python main.py file_name")

#stocke les rides pour les supprimer petit a petit
available_rides = info['rides']
ride_assignment = []
timer = []

#initialisation step
for vehicle_number in range(info['vehicles']):
    best_ride = find_best_ride(vehicle_number, available_rides)
    ride_assignment += [[best_ride]]
    timer += [setTimer(vehicle_number, best_ride, 0, ride_assignment, available_rides)]
    update_available_rides(available_rides, best_ride)

#boucle sur le temps (chaque étapes)
for time in range(info['steps']):
    # decrease the value of the timers
    TempsSuivant(TableauTimer)
    #trouve les vehicule ayant fini
    finished_vehicles = check(timer)
    for vehicle_number in finished_vehicles:
        #toruve le prochain best ride
        best_ride = find_best_ride(vehicle_number, available_rides)
        #ajoute le meilleur ride trouvé
        ride_assignment[vehicle_number] += [best_ride]
        #reset le temps
        timer[vehicle_number] = ride_time(best_ride)



#on va maintenant optimiser

#le nombre d'iteration de l'optiisation du score
total_steps = 1000
constante = math.log(2)
#le score de l'assignment d'origine (mettre les arguments)
score = total_score()

def proba_selection(actual_step):
    return 1 - math.exp((-1)*constante/actual_step)

for actual_step in range(total_steps):
    #on bidouille de manière random les rides
    new_ride_assignment = modify(ride_assignment)
    if total_score(new_ride_assignment) > score:
        ride_assignment = new_ride_assignment
    else:
        if random.uniform(0, 1) < proba_selection(actual_step):
            ride_assignment = new_ride_assignment

#fin on a un ride assignment qui est meilleur (en théorie)
