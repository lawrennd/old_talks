#!/usr/bin/env python3

import sys
import _python.ndltalk as nt

filename = sys.argv[1]
fields = nt.header_fields(filename)
print(fields['date'])
            
