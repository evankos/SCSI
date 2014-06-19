import re
import sys
import operator
import difflib
def vectify(lst):
	global vector
	total = list()
	for item in lst:
		if (item in vector):
			total = total + [vector.index(item)]
		else:
			vector = vector + [item]
			total = total + [vector.index(item)]
	total.sort()
	ret='';
	used= list()
	for item in total:
		times=total.count(item)
		if item not in used:
			used = used + [item]
			ret = ret + str(item) + ':' + str(times) + ' '
	# total = re.sub('(\d*)',r'\1:1',' '.join(str(x) for x in total))
	return ret
def standartize_tree(tree):
	tags=re.findall('\((\w+?)\s',tree)
	tags=list(set(tags))
	global tree_standards
	for tag in tags:
		standard_tags=difflib.get_close_matches(tag,tree_standards)
		try:
			tree = tree.replace('('+tag,'('+standard_tags[0])
		except IndexError:
			tree = tree.replace('('+tag,'(SBAR')	
	return tree
thelist=['1000','2000']
with open('/root/classification/pyStatParser-master/tree_standards') as fil1:
		tree_standards=fil1.read().split("\n")
vector = ['placeholder_displacement']
for fil in thelist:
	dict_total=dict()
	dict_fine=dict()
	index=1
	index1=1
	with open('train_'+ fil +'_final.tree') as f:
		totals=f.read()
	data = re.findall('(\w*?):(\w*?)\s+([^\n]*?)\n', totals)
	for dt in data:
		if dt[0] not in dict_total:
			dict_total[dt[0]]=index1
			index1 += 1
			for dt1 in data:
				if (dt1[0]==dt[0]):
					if dt1[0]+':'+dt1[1] not in dict_fine:
						dict_fine[dt1[0]+':'+dt1[1]]=index
						index += 1
		with open('train_'+ fil +'_tainset.dict', 'a') as f1:
			tree = re.findall('(\w+?)\)', dt[2].replace(') (',')(').lower())
			f1.write(str(dict_fine[dt[0]+':'+dt[1]] - 3)+' |BT| '+dt[2].replace(') (',')(') +" |ET| "+"\n")
		with open('train_'+ fil +'_tainset_coarse.dict', 'a') as f1:
			tree = re.findall('(\w+?)\)', dt[2].replace(') (',')(').lower())
			f1.write(str(dict_total[dt[0]] - 3)+' 	|BT| ' + dt[2].replace(') (',')(') + " |ET| "+"\n")
	sort_lst=sorted(dict_fine.iteritems(), key=operator.itemgetter(1))
	sort_lst1=sorted(dict_total.iteritems(), key=operator.itemgetter(1))
	with open('train_'+ fil +'.dict', 'a') as f1:
		for tup in sort_lst:
			f1.write(tup[0] +"\n")
	with open('train_'+ fil +'_coarse.dict', 'a') as f1:
		for tup in sort_lst1:
			f1.write(tup[0] +"\n")
with open('vector.vec','w') as f:
	f.write("\n".join(vector))