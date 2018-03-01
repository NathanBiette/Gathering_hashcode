class GatheringParser:
	def parse(self, input_file):
		file = open(input_file, 'r')
		print(file.read())
		file.close()