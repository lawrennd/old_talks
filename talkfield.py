#!/usr/bin/env python3

import sys
import os
import _python.ndltalk as nt

field = sys.argv[1]
filename = sys.argv[2]


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
            
