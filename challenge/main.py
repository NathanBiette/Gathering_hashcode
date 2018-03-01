from gathering_parser import GatheringParser as Parser
from submission import generate_output_file as got
import sys
import re

parser = Parser()
if len(sys.argv) == 2:
	parser.parse(sys.argv[1])
else:
	print("Syntax error:\r\nUsage : python main.py file_name")
	exit()
splited_path = re.split('/|\.', sys.argv[1])
file_name = splited_path[len(splited_path) - 2] # just before the .in extension
got([[0, 3, 4], [1, 2]], file_name)
