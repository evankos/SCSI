import re
import sys
import nltk
def merge_list(first_list,second_list):
	in_first = set(first_list)
	in_second = set(second_list)
	in_second_but_not_in_first = in_second - in_first
	result = first_list + list(in_second_but_not_in_first)
	return result

thelist=['1000','2000']
L=list()
for fil in thelist:
	with open('/root/classification/datasets/train_'+ fil +'.label') as f:
		file = f.read().lower()
		data = re.findall('\w*?:\w*?\s+([^\n]*?)\n', file)
		L1 = "\n".join(data)
		datas = nltk.word_tokenize(L1)
		datas = list(set(datas))
	with open('vector.vec','a') as f:
		f.write("\n".join(list(set(datas) - set(L))))
	L = list(set(L + datas))	