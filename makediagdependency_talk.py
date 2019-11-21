#!/usr/bin/env python3

import sys
import _python.ndltalk as nt

filename = sys.argv[1]
diagrams = nt.extract_diagrams(filename)
print(' '.join(diagrams))
