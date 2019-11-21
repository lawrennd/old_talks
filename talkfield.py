#!/usr/bin/env python3

import sys
import _python.ndltalk as nt
import yaml
from datetime import date

field = sys.argv[1]
filename = sys.argv[2]
answer = nt.talk_field(field, filename)

if field=='categories':
    print("['" + "', '".join(answer) + "']")
else:
    print(answer)
            
