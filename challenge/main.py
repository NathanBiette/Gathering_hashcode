from gathering_parser import GatheringParser as Parser
import sys

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
    timer += [ride_time(best_ride)]
    #il faut trouver un moyen de supprimer le ride de la liste des available une fois trouvé et assigné

#boucle sur le temps (chaque étapes)
for time in range(info['steps']):
    #trouve les vehicule ayant fini
    finished_vehicles = check(timer)
    for vehicle_number in finished_vehicles:
        #toruve le prochain best ride
        best_ride = find_best_ride(vehicle_number, available_rides)
        #ajoute le meilleur ride trouvé
        ride_assignment[vehicle_number] += [best_ride]
        #reset le temps
        timer[vehicle_number] = ride_time(best_ride)