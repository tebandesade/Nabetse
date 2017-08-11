# -*- encoding: utf-8 -*-
import sys
import codecs
import re
pags = [] 
file_ = sys.argv[1]
with codecs.open(file_, encoding='latin-1') as arch:
	temp = [] 
	for line in arch:	
		texto = line.strip()
		if not re.match(r'^\s*$', texto):
			temp.append(texto)	
			print ('test %%%: ', texto)
			if "P\xc3\xa1gin" in texto:
				temp.append(texto)
				pags.append(temp)
				temp = []
print(len(pags))
