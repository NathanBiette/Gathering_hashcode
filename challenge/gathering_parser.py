class GatheringParser:
	def parse(self, input_file):
		file = open(input_file, 'r')
		
		# Get datas
		lines = file.readlines()
		first_datas = lines[0].split()
		rides = []
		for line in lines[1:]:
			line_datas = line.split()
			infos = {
				'pos_start': (int(line_datas[0]), int(line_datas[1])),
				'pos_finish': (int(line_datas[2]), int(line_datas[3])),
				'start': int(line_datas[4]),
				'finish': int(line_datas[5]),
				'is_complete': False
			}
			rides.append(infos)

		file.close()

		return ({
			'rows': int(first_datas[0]),
			'columns': int(first_datas[1]),
			'vehicles': int(first_datas[2]),
			'nb_rides': int(first_datas[3]),
			'bonus': int(first_datas[4]),
			'steps': int(first_datas[5]),
			'rides': rides
			})