from gathering_parser import GatheringParser as Parser
import sys

parser = Parser()
if len(sys.argv) == 2:
	print(parser.parse(sys.argv[1]))
else:
	print("Syntax error:\r\nUsage : python main.py file_name")