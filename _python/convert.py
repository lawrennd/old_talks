#!/usr/bin/env python

import stringcase
import tokenize
from tokenize import NUMBER, STRING, NAME, OP, COMMENT

def handle_token(typ, token, srowcols, erowcols, line):
    (srow, scol) = srowcols
    (erow, ecol) = erowcols
    tok = repr(token)
    if typ == NAME:
        token = stringcase.snakecase(token)
    return (typ, token, srowcols, erowcols, line)


import sys

result = []
f = open(sys.argv[1])
g = tokenize.generate_tokens(f.readline) 
for typ, token, srowcols, erowcols, line  in g:
    result.append(handle_token(typ, token, srowcols, erowcols, line))

print(tokenize.untokenize(result))

    # lines = f.readlines()
# for line in lines:
#     split_line = line.split(' ')
    
#     print(stringcase.snakecase(line))

f.close()




