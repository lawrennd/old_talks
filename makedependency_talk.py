#!/usr/bin/env python

import sys
import ._python.ndltex as latex
import os

def readlines(filename):
    return lines

def extract_inputs(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    filenames = latex.extract_inputs(lines)
    list_files=[]
    for i, filename in enumerate(filenames):
        includepos = os.path.join('../', filename)
        if os.path.isfile(filename):
            list_files.append(filename)
        elif os.path.isfile(includepos):
            list_files.append(includepos)
        else:
            list_files.append(filename)
    filenames = list_files

    for i, filename in enumerate(filenames):
        if os.path.isfile(filename):
            list_files[i+1:i+1] = extract_inputs(filename) 
    return list_files

filename = sys.argv[1]
listfiles = extract_inputs(filename)
print(filename + ' ' + ' '.join(listfiles))
