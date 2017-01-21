#!/usr/bin/env python3
# translate bf programs to psh

import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="input a pipeslash file")
args = parser.parse_args()

def file_to_string():
	with open(args.inputfile, 'r') as myfile:
		data=myfile.read().replace('\n', '')
	return data

infileraw = re.sub('[^/|\|]', '', file_to_string())
infile = re.sub(r'(?<!/)/(?!/)', '', infileraw).replace('//', ' ')

dic = {'|':'>',
	 '||':'<',
	 '|||':'+',
	 '||||':'-',
	 '|||||':'.',
	 '||||||':',',
	 '|||||||':'[',
	 '||||||||':']',
	 'sep':' ',
}

try: infile = infile.split(dic['sep'])
except ValueError: pass

outfile=''
for x in infile:
	if x in dic:
		outfile += dic[x]
	else:
		outfile += x
print(outfile)
