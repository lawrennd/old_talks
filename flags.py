#!/usr/bin/env python3

import argparse
import os
import _python.ndltalk as nt
import _python.ndlyaml as ny


parser = argparse.ArgumentParser()
parser.add_argument("output",
                    type=str,
                    choices=['pp', 'post', 'docx', 'pptx', 'prefix', 'reveal'],
                    help="The type of output file (post is for a jekyll post, docx for word, pptx for powerpoint)")
parser.add_argument("base",
                    type=str,
                    help="The base part of the filename")


args = parser.parse_args()

filename = args.base + '.md'

fields = ny.header_fields(filename)

try:
    date = ny.header_field('date', fields).strftime("%Y-%m-%d")
except ny.FileFormatError:
    date = None

try:
    week = int(ny.header_field('week', fields))
    weekarg = """ --metadata week={week}""".format(week=week)
except ny.FileFormatError:
    week = 0
    weekarg = ''

try:
    session = int(ny.header_field('session', fields))
    sessionarg = """ --metadata session={session}""".format(session=session)
except ny.FileFormatError:
    session = 0
    sessionarg = ''

try:
    background = int(ny.header_field('background', fields))
    backgroundarg = """ --metadata background={background}""".format(background=background)
except ny.FileFormatError:
    background = 0
    backgroundarg = ''

try:
    revealjs_url = ny.header_field('revealjs_url', fields)
except ny.FileFormatError:
    revealjs_url = 'https://unpkg.com/reveal.js@3.9.2'
revealjs_urlarg = """ --variable revealjs-url={revealjs_url}""".format(revealjs_url=revealjs_url)

try:
    revealjs_theme = ny.header_field('revealjs_theme', fields)
except ny.FileFormatError:
    revealjs_theme = 'black'
revealjs_themearg = """ --variable theme={revealjs_theme}""".format(revealjs_theme=revealjs_theme)

try:
    layout = ny.header_field('layout', fields)
except ny.FileFormatError:
    layout = 'talk'

if layout == 'lecture':
    prefix = ''
    if week>0:
        prefix += '{0:02}'.format(week)
    if session>0:
        if week>0:
            prefix += '-'
        prefix += '{0:02}'.format(session)
    prefix += '-'
elif layout == 'background':
    prefix = ''
    if week>0:
        prefix += '{0:02}'.format(week)
    if session>0:
        if week>0:
            prefix += '-'
        prefix += '{0:02}'.format(session)
    if background>0:
        if session>0:
            if week>0:
                prefix += '-'
            prefix += '{0:02}'.format(background)
    prefix += '-'
elif layout == 'test':
    prefix = 'XXXX-XX-XX'
    prefix += '-'
elif layout == 'talk':
    prefix = date
    prefix += '-'
elif layout == 'dataset':
    prefix = ''

out = prefix + args.base
    
if args.output == 'prefix':
    print(prefix)
    
elif args.output == 'post':
    if date is not None:
        lines = """--metadata date={date} """
    else:
        lines = ""
    for ext in ['docx', 'pptx']:
        if ny.header_field(ext, fields):
            lines += """ --metadata {ext}={{out}}.{ext}""".format(ext=ext)
    if ny.header_field('reveal', fields):
        lines += """ --metadata reveal={out}.slides.html"""
    if ny.header_field('ipynb', fields):
        lines += """ --metadata ipynb={out}.ipynb"""
    if ny.header_field('slidesipynb', fields):
        lines += """ --metadata slidesipynb={out}.slides.ipynb"""
    if ny.header_field('notespdf', fields):
        lines += """ --metadata notespdf={out}.notes.pdf"""
    if ny.header_field('pdf', fields):
        lines += """ --metadata pdf={out}.pdf"""
    if args.output == 'post':
        lines += weekarg + sessionarg + """ --metadata layout={layout}""".format(layout=layout)
    if ny.header_field('ghub', fields):
        ghub = ny.header_field('ghub', fields)[0]
        lines += """ --metadata edit_url={local_edit}""".format(local_edit="https://github.com/{ghub_organization}/{ghub_repository}/edit/{ghub_branch}/{ghub_dir}/{base}.md".format(base=args.base, ghub_organization=ghub['organization'], ghub_repository=ghub['repository'], ghub_branch=ghub['branch'], ghub_dir=ghub['directory']))    
    print(lines.format(out=out, date=date))

elif args.output=='docx':
    lines = '--reference-doc ' + ny.header_field('dotx', fields)
    print(lines)

elif args.output=='pptx':
    lines = '--reference-doc ' + ny.header_field('potx', fields)
    print(lines)

elif args.output=='reveal':
    lines = '--slide-level 2 ' + revealjs_urlarg + revealjs_themearg
    print(lines)


    
elif args.output=='pp':
    lines = '--include-path ./..'
    # Flags for the preprocessor.
    if ny.header_field('assignment', fields):
        lines += """ --assignment"""
    print(lines)
