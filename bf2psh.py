#!/usr/bin/env python3
# translate bf programs to psh

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="input a brainf**k file")
args = parser.parse_args()

def file_to_string():
	with open(args.inputfile, 'r') as myfile:
		data=myfile.read().replace('\n', '')
	return data

infile = file_to_string()

dic = {'>':'/|/',
	 '<':'/||/',
	 '+':'/|||/',
	 '-':'/||||/',
	 '.':'/|||||/',
	 ',':'/||||||/',
	 '[':'/|||||||/',
	 ']':'/||||||||/',
}

outfile=''
for x in infile:
	if x in dic:
		outfile += dic[x]
	else:
		outfile += x
print(outfile)
