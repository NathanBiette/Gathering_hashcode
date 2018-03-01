output_dir = 'output/'

def generate_output_file(rides_by_vehicles, file_name):
	with open(output_dir + file_name + ".out", 'w') as output_file:
		for vehicle in rides_by_vehicles:
			output_file.write(str(len(vehicle)) + ' ')
			for ride in vehicle:
				output_file.write(str(ride))
			output_file.write('\n')