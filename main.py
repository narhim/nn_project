#Import modules
import re
import csv

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

#Write tsv file
with open('sample.tsv','r',encoding="utf-8") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    maximum=0
    minimum=0
    mean=0
    count_seq=0
   
    temp=0
    pos_dict={}
    pos_lost=[]
    for line in tsvreader:
    	# ignoring sequence separator '*'
        if line[0]!="*":
            if int(line[0])>maximum:
                maximum=int(line[0])
                if count_seq==0:
                    minimum=maximum
            temp=int(line[0]) 
            
            # creating dictionary of pos
            
            if line[-1] not in pos_dict.keys():
                pos_dict[line[-1]]=1
            else:
                pos_dict[line[-1]]+=1
        else:
            count_seq+=1
            mean+=temp
            if temp<minimum:
                minimum=temp
        
    
for k in pos_dict:
    pos_dict[k]=pos_dict[k]/sum(pos_dict.values())

#writing these info into a file
with open("sample.info","w",encoding="utf-8") as f:
    print("Max sequence length: ",maximum,file=f)
    print("Min sequence length: ",minimum,file=f)
    print("Mean sequence length: ",mean,file=f)
    print("Number of sequences: ",count_seq,file=f)
    print("Tags: ",file=f)
    for k,v in pos_dict.items():
        print(k+"\t"+str(v),file=f)
    
