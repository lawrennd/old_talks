#!/usr/bin/env python3

import argparse
import _python.ndltalk as nt

parser = argparse.ArgumentParser()
parser.add_argument("dependency",
                    type=str,
                    choices=['all', 'diagrams', 'inputs', 'bibinputs', 'slidediagrams'],
                    help="The type of dependency that is required")
parser.add_argument("filename",
                    type=str,
                    help="The filename where dependencies are being searched")


args = parser.parse_args()

if args.dependency == 'all':
    listfiles = nt.extract_all(args.filename)
    print(' '.join(listfiles))

elif args.dependency == 'diagrams':
    listfiles = nt.extract_diagrams(args.filename)
    print(' '.join(listfiles))

elif args.dependency == 'slidediagrams':
    listfiles = nt.extract_diagrams(args.filename, absolute_path=False, diagram_exts=['svg'])
    print(' '.join(listfiles))
    
elif args.dependency == 'inputs':    
    listfiles = nt.extract_inputs(args.filename)
    print(args.filename + ' ' + ' '.join(listfiles))

elif args.dependency == 'bibinputs':
    listfiles = nt.extract_bibinputs(args.filename)
    print(' '.join(listfiles))

    
