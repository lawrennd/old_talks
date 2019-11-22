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
    --metadata {ext}={{out}}.{ext}""".format(ext=ext)
    if nt.header_field('reveal', fields):
        lines += """\
    --metadata reveal={out}.slides.html"""
    if nt.header_field('ipynb', fields):
        lines += """\
    --metadata ipynb={out}.ipynb"""
    if nt.header_field('slidesipynb', fields):
        lines += """\         
    --metadata slidesipynb={out}.slides.ipynb"""
    if nt.header_field('notespdf', fields):
        lines += """\        
    --metadata notespdf={out}.notes.pdf"""
    if nt.header_field('pdf', fields):
        lines += """\        
    --metadata pdf={out}.pdf"""

    lines+="""\
    --metadata published={date}"""
    
    print(lines.format(out=out, date=date))

if output=='docx':
    lines = '--reference-doc ' + nt.header_field('dotx', fields)
    print(lines)

if output=='pptx':
    lines = '--reference-doc ' + nt.header_field('potx', fields)
    print(lines)
    
