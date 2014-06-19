from nltk.tree import *
from nltk.draw import tree
import re
import pickle
import sys
import subprocess
def echo(s):
	print s
def List_To_Tree(lst):
	if(not isinstance(lst, basestring)):
		if(len(lst) == 2 and isinstance(lst[0], basestring) and isinstance(lst[1], basestring)):				
			lst = Tree(str(lst[0]).split('+')[0],[str(lst[1])])
		elif(isinstance(lst[0], basestring) and not isinstance(lst[1], basestring)):
			lst = Tree(str(lst[0]).split('+')[0],map(List_To_Tree, lst[1: len(lst) ]))
	return lst
thelist=['1000','2000']	
for fil in thelist:
	subprocess.call(["/root/classification/Python-2.7.6/python", "parse.py",fil])
	with open('train_'+ fil +'.tree', 'r') as f:
		data=f.read()
	parsed = re.findall('(\w*?:\w*?)\s+\[\[ss([\s\S]*?)ss\]\]', data)
	for lis in parsed:
		lis_parsed=pickle.loads(lis[1])
		tr = Tree.pprint(List_To_Tree(lis_parsed),9999)
		print (tr)
		with open('train_'+ fil +'_final.tree', 'a') as f1:
			f1.write(lis[0] + ' ' + tr + "\n")	
import dictify.py