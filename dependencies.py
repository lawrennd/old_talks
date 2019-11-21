#!/usr/bin/env python3

import sys
import _python.ndltalk as nt

dependency = sys.argv[1]
filename = sys.argv[2]

if dependency == 'all':
    listfiles = nt.extract_all(filename)
    print(' '.join(listfiles))

elif dependency == 'diagrams':
    listfiles = nt.extract_diagrams(filename)
    print(' '.join(listfiles))
    
elif dependency == 'inputs':    
    listfiles = nt.extract_inputs(filename)
    print(filename + ' ' + ' '.join(listfiles))

elif dependency == 'bibinputs':
    listfiles = nt.extract_bibinputs(filename)
    print(' '.join(listfiles))

    
