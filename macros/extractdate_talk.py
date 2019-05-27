#!/usr/bin/env python

import sys
import _python.ndltex as latex
import os

import yaml

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

import re

filename = sys.argv[1]
md = open(filename, 'r')
text = md.read()
md.close()
# Returns first yaml content, `--- yaml frontmatter ---` from the .md file
# http://regexr.com/3f5la
# https://stackoverflow.com/questions/2503413/regular-expression-to-stop-at-first-match
match = re.findall('^---[\s\S]+?---', text)
if match:
    # Strips `---` to create a valid yaml object
    ymd = match[0].replace('---', '')
    print(yaml.load(ymd)['date'])
            
