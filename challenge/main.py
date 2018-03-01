from gathering_parser import GatheringParser as Parser
from submission import generate_output_file as got
import sys
import re
from math import *
import random
from Utilities import *
from score import *

parser = Parser()
if len(sys.argv) == 2:
	info = parser.parse(sys.argv[1])
else:
	print("Syntax error:\r\nUsage : python main.py file_name")
	exit()
splited_path = re.split('/|\.', sys.argv[1])
file_name = splited_path[len(splited_path) - 2] # just before the .in extension

#stocke les rides pour les supprimer petit a petit
available_rides = info['rides']
ride_assignment = []
timer = []

#initialisation step
for vehicle_number in range(info['vehicles']):
    best_ride = find_best_ride(vehicle_number,timer, info['bonus'], ride_assignment, available_rides)
    ride_assignment += [[best_ride]]
    timer += [setTimer(vehicle_number, best_ride, 0, ride_assignment, available_rides)]
    available_rides[best_ride]['is_complete'] = True

#boucle sur le temps (chaque étapes)
for time in range(info['steps']):
    # decrease the value of the timers
    TempsSuivant(TableauTimer)
    #trouve les vehicule ayant fini
    finished_vehicles = check(timer)
    for vehicle_number in finished_vehicles:
        #toruve le prochain best ride
        best_ride = find_best_ride(vehicle_number,timer, info['bonus'], ride_assignment, available_rides)
        #ajoute le meilleur ride trouvé
        ride_assignment[vehicle_number] += [best_ride]
        available_rides[best_ride]['is_complete'] = True
        #reset le temps
        timer[vehicle_number] = setTimer(vehicle_number, best_ride, time, ride_assignment, available_rides)



#on va maintenant optimiser

#le nombre d'iteration de l'optiisation du score
total_steps = 1000
constante = math.log(2)
#le score de l'assignment d'origine (mettre les arguments)
score = totalScore(ride_assignment, info['bonus'], available_rides)

def proba_selection(actual_step):
    return 1 - math.exp((-1)*constante/actual_step)

for actual_step in range(total_steps):
    #on bidouille de manière random les rides
    new_ride_assignment = modify(ride_assignment)
    if totalScore(ride_assignment, info['bonus'], available_rides) > score:
        ride_assignment = new_ride_assignment
    else:
        if random.uniform(0, 1) < proba_selection(actual_step):
            ride_assignment = new_ride_assignment

#fin on a un ride assignment qui est meilleur (en théorie)
got(ride_assignment, file_name)