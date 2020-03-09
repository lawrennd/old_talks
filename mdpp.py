#!/usr/bin/env python3
# Markdown Preprocessor for talks.
# Requries gpp (the generic preprocessor) to be installed.

import argparse
import _python.ndltalk as nt

parser = argparse.ArgumentParser()

parser.add_argument("filename", type=str,
                    help="Input filename")

parser.add_argument("-o", "--output", type=str,
                    help="Output filename")

parser.add_argument("--no-header", default=False, action='store_true',
                    help="Whether to search for a header in the input file (default False).")

parser.add_argument("-B", "--include-before-body", type=str,
                    help="File to include before body.")

parser.add_argument("-A", "--include-after-body", type=str,
                    help="File to include after body.")

parser.add_argument("-t", "--to", type=str,
		    choices=['pptx', 'html', 'docx', 'ipynb', 'svg', 'tex'],
                    help="Target ouptut file format")

parser.add_argument("-I", "--include-path", type=str,
                    help="include diractories")

parser.add_argument("-F", "--format", type=str,
		   choices=['notes', 'slides'],
		   help="Target output file contents")


args = parser.parse_args()

arglist = ['-U "\\\\" "" "{" "}{" "}" "{" "}" "#" ""']
if args.to:
   arglist.append('-D{to}=1'.format(to=args.to.upper()))
if args.format:
   arglist.append('-D{format}=1'.format(format=args.format.upper()))
if args.include_path:
   arglist.append('-I{include}'.format(include=args.include_path))
if args.output:
   arglist.append('-o {}'.format(args.output))
   
filelist = []
if args.include_before_body:
   with open(args.include_before_body, 'r') as fd:
      before_text = fd.read()
else:
   before_text = ''

if args.include_after_body:
   with open(args.include_after_body, 'r') as fd:
      after_text = fd.read()
else:
   after_text = ''

if args.no_header:
   md= open(args.filename, 'r')
   body = md.read()
   md.close()
else:
   header,body = nt.extract_header_body(args.filename)


with open('tmp.md','w') as fd:
   if not args.no_header:
      fd.write('---')
      fd.write(header)
      fd.write('---\n')
   
   fd.write(before_text)
   fd.write(body)
   fd.write(after_text)


import os
runlist = ['gpp'] + arglist + ['tmp.md']
print(' '.join(runlist))
os.system(' '.join(runlist))
os.system('rm tmp.md')
#gpp  -DPPTX=1 -DSLIDES=1 ${PPFLAGS} --include ../_includes/talk-notation.tex $< -o $output
