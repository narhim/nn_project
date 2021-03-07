# Import modules
import os
import argparse
import re
import csv
import sys


def simplify_datafile(args):
    """
    Simplify sample.conll file to get rid of unnecessary columns, then write the simplified data to sample.tsv

    :param args:
    :return:
    """
    # Read Conll file:
    with open(args.dataset_name, "r", encoding="utf-8") as file:
        # list where all the relevant information will be stored
        corpus = []
        for line in file:
            # Ignore lines whic start with '#' (begin/end document).
            if re.match('#', line):
                continue
            # If line is empty, append * to indicate end of sequence.
            elif re.search('^\n', line):
                corpus.append('*\n')
            # Else, split line by white space, store position, word and tag on a string separated by tabs. Save in
            # corpus.
            else:
                w = line.split()
                word = w[2] + '\t' + w[3] + '\t' + w[4] + '\n'
                corpus.append(word)

    # Write tsv file
    result_file_path = os.path.join(args.output_dir, args.output_filename)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

    with open(result_file_path, 'w+', encoding="utf-8") as file:
        for line in corpus:
            file.write(line)


def generate_info_file(args):
    """
    generate sample.info containing dataset statistics. This function can only be run after
    the output file from simply_datafile function has been generated.

    :param args: parsed commandline argument containing output_dir and output_filename
    :return:
    """

    # increase csv field size limit otherwise large fields will throw an error
    csv.field_size_limit(sys.maxsize)
    result_file_path = os.path.join(args.output_dir, args.output_filename)
    # reading from sample.tsv
    with open(result_file_path, 'r', encoding="utf-8") as tsvfile:
        tsvreader = csv.reader(tsvfile, delimiter="\t")

        # initializing variables that are going to be used later
        maximum = 0
        minimum = 0
        mean = 0
        count_seq = 0
        temp = 0
        pos_dict = {}
        pos_lost = []

        for line in tsvreader:

            # ignoring sequence separator '*'
            if line[0] != "*":
                if int(line[0]) > maximum:
                    maximum = int(line[0])
                    if count_seq == 0:
                        minimum = maximum
                temp = int(line[0])+1

                # creating dictionary of pos

                if line[-1] not in pos_dict.keys():
                    pos_dict[line[-1]] = 1
                else:
                    pos_dict[line[-1]] += 1
            else:
                # counting the number of sequences, via the number of "*" encountered
                count_seq += 1
                mean += temp
                if temp < minimum:
                    minimum = temp
    # calculating the final values
    mean=mean/count_seq
    
    # taking into account the word at index '0'
    maximum+=1 
    minimum+=1
    for k in pos_dict:
        pos_dict[k] = pos_dict[k] / sum(pos_dict.values())

    # writing these info into a file
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    info_file_path = os.path.join(args.output_dir, args.info_filename)
    with open(info_file_path, "w+", encoding="utf-8") as f:
        print("Max sequence length: ", maximum, file=f)
        print("Min sequence length: ", minimum, file=f)
        print("Mean sequence length: ", mean, file=f)
        print("Number of sequences: ", count_seq, file=f)
        print("Tags: ", file=f)
        for k, v in pos_dict.items():
            print(k + "\t" + str(v), file=f)


def main():
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='data_preprocess.py', description='Preprocessing Steps: simplify conll '
                                                                               'dataset and obtain dataset statistics')
    # Add the arguments
    my_parser.add_argument('--dataset_name', required=True, default='sample.conll',
                           help='Conll datafile to be pre-processed')
    my_parser.add_argument('--output_dir', required=True, default='results',
                           help='Directory name to save the pre-processed and info files')
    my_parser.add_argument('--info_filename', default='sample.info', help='Filename to save data statistics')
    my_parser.add_argument('--output_filename', default='sample.tsv', help='Filename to save the pre-processed file')
    my_parser.add_argument('--both', type=bool, default=True, help='Perform both simplify and generated info file steps')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    simplify_datafile(args)

    if args.both:
        generate_info_file(args)


if __name__ == '__main__':
    main()
