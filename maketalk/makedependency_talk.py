#!/usr/bin/env python3

import sys
import _python.ndltalk as nt

filename = sys.argv[1]
listfiles = nt.extract_inputs(filename)
print(filename + ' ' + ' '.join(listfiles))
