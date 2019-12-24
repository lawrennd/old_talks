#!/usr/bin/env python3

import argparse
import os
import _python.ndltalk as nt


parser = argparse.ArgumentParser()
parser.add_argument("output",
                    type=str,
                    choices=['post', 'docx', 'pptx'],
                    help="The type of output file (post is for a jekyll post, docx for word, pptx for powerpoint)")
parser.add_argument("base",
                    type=str,
                    help="The base part of the filename")


args = parser.parse_args()

filename = args.base + '.md'

fields = nt.header_fields(filename)
date = nt.header_field('date', fields).strftime("%Y-%m-%d")
out = date + '-' + args.base

if args.output == 'post':
    lines = """--metadata date={date} --metadata layout=talk"""
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
    
    print(lines.format(out=out, date=date))

if args.output=='docx':
    lines = '--reference-doc ' + nt.header_field('dotx', fields)
    print(lines)

if args.output=='pptx':
    lines = '--reference-doc ' + nt.header_field('potx', fields)
    print(lines)
    
