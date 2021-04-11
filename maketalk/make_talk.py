#!/usr/bin/env python3

import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename",
                    type=str,
                    help="The filename where dependencies are being searched")

args = parser.parse_args()

basename = os.path.basename(args.filename)
base = os.path.splitext(basename)[0]

f = open('makefile', 'w+')
f.write('BASE={filename}\n'.format(filename=base))
f.write('include ../make-talk-flags.mk\n')
f.write('include ../make-talk.mk\n')
f.close()

os.system('git pull')
os.system('make all')
