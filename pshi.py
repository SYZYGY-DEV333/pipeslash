#!/usr/bin/env python3
# Crappy Pipeslash interpreter

# Copyright (c) 2017, SYZYGY-DEV333
# All rights reserved.
# Licensed under SPL 1.0 [splicense.pen.io]

import argparse
import re


# Parser

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


# Interpreter

def interpret(code):
  tape = [0]*(3*10**4)
  ptr = 0
  loops = []
  i = 0
  res = ""
  while i < len(code):
    c = code[i]
    #parse the operators, update the tape
    if c == "+":
      tape[ptr] = (tape[ptr] + 1) % 256
    elif c == "-":
      tape[ptr] = (tape[ptr] - 1) % 256
    elif c == ">":
      ptr += 1
      if ptr >= len(tape):
        raise ValueError('Segmentation fault')
    elif c == "<":
      ptr -= 1
      if ptr < 0:
        raise ValueError('Segmentation fault')
    elif c == ".":
      res += chr(tape[ptr])
    elif c == ",":
      c = ord(sys.stdin.read(1))
      if c != 26:
          tape[ptr] = c
    elif c == "[":
      #Check the tape
      if tape[ptr] > 0:
        #Add the index to the stack
        loops.append(i - 1)
      else:
        #Find the closing brace with a stack operation (get m to be 0)
        m = 1
        j = i + 1
        while j < len(code) and m > 0:
          if code[j] == "[":
            m += 1
          elif code[j] == "]":
            m -= 1
          j += 1
        if m > 0:
          raise ValueError('Mismatched loops')
        #move the loop
        i = j - 1
    elif c == "]":
      if len(loops) == 0:
        raise ValueError('Mismatched loops')
      #go back to the start of the loop
      i = loops.pop()
    i += 1
  return res

if __name__=="__main__":
  import sys
  print(interpret(outfile))
