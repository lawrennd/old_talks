#!/usr/bin/env python3

import sys
import os
import _python.ndltalk as nt



output = sys.argv[1]
base = sys.argv[2]
filename = base + '.md'

fields = nt.header_fields(filename)
date = nt.header_field('date', fields).strftime("%Y-%m-%d")
out = date + '-' + base

if output == 'post':
    lines = """--metadata date={date} \
    --metadata layout=talk"""
    for ext in ['docx', 'pptx']:
        if nt.header_field(ext, fields):
            lines += """\
    --metadata reveal={{out}}.{ext}""".format(ext=ext)
    if nt.header_field('pptx', fields):
        lines += """\
        \
    --metadata notesipynb={out}.ipynb \
    --metadata slidesipynb={out}.slides.ipynb \
    --metadata notespdf={out}.notes.pdf \
    --metadata slidespdf={out}.pdf \
    --metadata docx={out}.notes.docx \

    --metadata published={date}"""

    print(lines.format(out=out, date=date))

if output=='docx':
    lines = '--reference-doc ' + nt.header_field('dotx', fields)
    print(lines)

if output=='pptx':
    lines = '--reference-doc ' + nt.header_field('potx', fields)
    print(lines)
    
