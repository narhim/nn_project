#Import modules
import os
import argparse
import re
import csv


def main():
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='data_preprocess',description='data preprocessing')            
    # Add the arguments
    my_parser.add_argument('--dataset_name', required=True)
    my_parser.add_argument('--output_dir', required=True)

    # Execute the parse_args() method
    args = my_parser.parse_args()

    input_file = args.dataset_name
    output_dir=args.output_dir



    #Read Conll file:
    with open(input_file,"r",encoding = "utf-8") as file:
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
    result_filename='sample.tsv'
    result_fullname = os.path.join(output_dir, result_filename)
    with open(result_fullname,'w',encoding="utf-8") as file:
    	for line in corpus:
    		file.write(line)

    #generate the info file
    with open(result_fullname,'r',encoding="utf-8") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")

        # initializing variables that are going to be used later
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
                # counting the number of sequences, via the number of "*" encountered
                count_seq+=1
                mean+=temp
                if temp<minimum:
                    minimum=temp
            
        
    for k in pos_dict:
        pos_dict[k]=pos_dict[k]/sum(pos_dict.values())

    #writing these info into a file
    info_filename="sample.info"
    info_fullname=os.path.join(output_dir, info_filename)
    with open(info_fullname,"w",encoding="utf-8") as f:
        print("Max sequence length: ",maximum,file=f)
        print("Min sequence length: ",minimum,file=f)
        print("Mean sequence length: ",mean,file=f)
        print("Number of sequences: ",count_seq,file=f)
        print("Tags: ",file=f)
        for k,v in pos_dict.items():
            print(k+"\t"+str(v),file=f)
    
if __name__=="main":
    main()