#!/usr/bin/env python3

import sys
import _python.ndltex as latex
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
    filenames = list_files
    
    for i, filename in enumerate(filenames):
        list_files[i+1:i+1] = extract_inputs(filename) 

    return list_files

filename = sys.argv[1]
filenames = [filename] + extract_inputs(filename)

listdiagrams = []
for filename in filenames:
    if filename[:14] =='../talk-macros':
        continue
    
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    for ext in ['png', 'jpg', 'gif']:
        diagrams = latex.extract_diagrams(lines, ext)
        diag_list = []
        for i, diag_str in enumerate(diagrams):
            if "\\" not in diag_str:
                diag_list.append(diag_str + '.' + ext)
        listdiagrams.extend(diag_list)
    diagrams = latex.extract_diagrams(lines, 'diagram')
    png_list = []
    pdf_list = []
    diag_list = []
    for i, diag_str in enumerate(diagrams):
        if "\\" not in diag_str:
            diag_list.append(diag_str + '.svg')
            png_list.append(diag_str + '.png')
            pdf_list.append(diag_str + '.pdf')
    
    listdiagrams.extend(diag_list)
    listdiagrams.extend(png_list)
    listdiagrams.extend(pdf_list)

full_list = []
for diag in listdiagrams:
    full_list.append(os.path.abspath(diag))
print(' '.join(full_list))
