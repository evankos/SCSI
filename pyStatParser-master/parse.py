import pickle
import re
from stat_parser.parser import Parser
import sys
parser = Parser()
	
with open('/root/classification/datasets/train_'+ sys.argv[1] +'.label') as f:
	for line in f:
		data = re.findall('(\w*?:\w*?)\s+(.*)', line)
		with open('train_'+ sys.argv[1] +'.tree', 'a') as f1:
			f1.write(data[0][0] + ' [[ss')
			ssd=parser.norm_parse(data[0][1])
			pickle.dump(ssd, f1)
			f1.write('ss]]')
			print data[0][1]