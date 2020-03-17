#!/usr/bin/env python3

import sys
import _python.ndltalk as nt
import yaml
from datetime import date

field = sys.argv[1]
filename = sys.argv[2]

defaults = {'slidedir': '../slides/',
            'notedir': '../_notes/',
            'notebookdir': '../_notebooks/',
            'postdir': '../_posts/',
            'week': 0}

try:
    answer = nt.talk_field(field, filename)
except nt.FileFormatError:
    if field in defaults:
        answer= defaults[field]
    else:
        answer = ''
        
if field=='categories':
    print("['" + "', '".join(answer) + "']")
else:
    print(answer)
            
