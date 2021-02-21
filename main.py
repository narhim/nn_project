#Import modules
import re

#Read Conll file:
with open('sample.conll',"r",encoding = "utf-8") as file:
	#list where all the relevant information will be stored
	corpus = []
	for line in file:
		#Ignore lines whic start with '#' (begin/end document).
		if re.match('#',line):
			continue
		#If line is empty, append * to indicate end of sequence.
		elif re.search('^\n',line):
			corpus.append('*\n')
		#Else, split line by white space, store position, word and tag on a string separated by tabs. Save in corpus.
		else:	
			w = line.split()
			word = w[2] + '\t' + w[3] + '\t' + w[4] + '\n'
			corpus.append(word)

#Write tsv file
with open('sample.tsv','w',encoding="utf-8") as file:
	for line in corpus:
		file.write(line)
