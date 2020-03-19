#!/usr/bin/env python3

import argparse
import os
import _python.ndltalk as nt


parser = argparse.ArgumentParser()
parser.add_argument("output",
                    type=str,
                    choices=['pp', 'post', 'docx', 'pptx', 'prefix'],
                    help="The type of output file (post is for a jekyll post, docx for word, pptx for powerpoint)")
parser.add_argument("base",
                    type=str,
                    help="The base part of the filename")


args = parser.parse_args()

filename = args.base + '.md'

fields = nt.header_fields(filename)
date = nt.header_field('date', fields).strftime("%Y-%m-%d")
try:
    week = int(nt.header_field('week', fields))
    weekarg = """ --metadata week={week}""".format(week=week)
except nt.FileFormatError:
    week = 0
    weekarg = ''

try:
    layout = nt.header_field('layout', fields)
except nt.FileFormatError:
    layout = 'talk'

if layout == 'lecture':
    prefix = '{0:02}'.format(week)
elif layout == 'test':
    prefix = 'XXXX-XX-XX'

out = prefix + '-' + args.base
    
if args.output == 'prefix':
    print(prefix)
    
elif args.output == 'post':
    lines = """--metadata date={date} """
    for ext in ['docx', 'pptx']:
        if nt.header_field(ext, fields):
            lines += """ --metadata {ext}={{out}}.{ext}""".format(ext=ext)
    if nt.header_field('reveal', fields):
        lines += """ --metadata reveal={out}.slides.html"""
    if nt.header_field('ipynb', fields):
        lines += """ --metadata ipynb={out}.ipynb"""
    if nt.header_field('slidesipynb', fields):
        lines += """ --metadata slidesipynb={out}.slides.ipynb"""
    if nt.header_field('notespdf', fields):
        lines += """ --metadata notespdf={out}.notes.pdf"""
    if nt.header_field('pdf', fields):
        lines += """ --metadata pdf={out}.pdf"""
    if args.output == 'post':
        lines += weekarg + """ --metadata layout={layout}""".format(layout=layout)
        
    print(lines.format(out=out, date=date))

elif args.output=='docx':
    lines = '--reference-doc ' + nt.header_field('dotx', fields)
    print(lines)

elif args.output=='pptx':
    lines = '--reference-doc ' + nt.header_field('potx', fields)
    print(lines)

elif args.output=='pp':
    lines = '--include-path ./..'
    # Flags for the preprocessor.
    if nt.header_field('assignment', fields):
        lines += """ --assignment"""
    print(lines)
