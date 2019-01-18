#!/usr/bin/env python

import re
import os

tex_directories = os.environ['BIBINPUTS'].split(':') + os.environ['TEXINPUTS'].split(':')
def replace_notation(tex_file_lines, old_notation, new_notation):
    #    openBracketList ='\(|\[|\{'
    #closeBracketList = '\)|\]|\}'
    #mathSymbol = '=|+|-\)|\]|\}'
    #subSuperList = '\^|_'
    #notationReg = '[' + openBracketList +'|'+ closeBracketList +'|' + subSuperList+'|'+ '\s' + oldNotation \^|_|\s|\]|\}|oldNotation
    filename = ''
    for line in tex_file_lines:
        filename = filename + line

    terminate = '[^\w|_]'
    start_math = re.escape('$')
    not_reg = re.compile(r'([' + start_math + ']' + '[^' + start_math + ']*' + terminate + ')' + old_notation + '(' + terminate + ')')
    matches = not_reg.findall(filename)
    return matches

def extract_bib_files(tex_file_lines):
    bib_files = []
    match_bib = re.compile(r"""\\bibliography{([^}]*)}""")
    match_bib2 = re.compile(r"""\\begin{btSect}.*{([^}]*)}""")
    for line in tex_file_lines.split('\n'):
       line_bib = match_bib.findall(line)
       if line_bib:
           for bib in line_bib:
               bib_files = bib_files + bib.split(',')
       line_bib2 = match_bib2.findall(line)
       if line_bib2:
           for bib in line_bib2:
               bib_files = bib_files + bib.split(',')

    return bib_files

def substitute_inputs(filename, directories=none):

    print filename
    file_dir = os.path.dirname(filename)
    if directories == none:
        directories = [file_dir]
        filename = os.path.basename(filename)
    elif len(file_dir)>0:
        if file_dir not in directories:
            directories.append(file_dir)

    for directory in tex_directories:
        if directory not in directories:
            directories.append(directory)
    if filename[0] == '#': # it's a macro
        return none
    tex_file_handle = none
    for directory in directories:
        full_filename = os.path.join(directory, filename)
        if os.path.exists(full_filename):
            tex_file_handle = open(full_filename, 'r')
            dirname = directory
            break
    if not tex_file_handle:
        return none
    tex_file_lines = tex_file_handle.readlines()
    new_lines = ''
    # Avoid parsing defined commands in notation def.
    for line in tex_file_lines:
        if not line[0] == '%':
            match_inp = re.compile(r"""\\newsection *{([^}]*)} *{([^}]*)}""")
            for match in match_inp.finditer(line):
                subs = substitute_inputs(input_file_name(match.group(2)), directories)
                if subs:
                    replace_string = '\\section{' + match.group(1) + '}' + '\n'*2 + subs
                    line = line.replace(match.group(0), replace_string)

            match_inp = re.compile(r"""\\newsubsection *{([^}]*)} *{([^}]*)}""")
            for match in match_inp.finditer(line):
                subs = substitute_inputs(input_file_name(match.group(2)), directories)
                if subs:
                    replace_string = '\\subsection{' + match.group(1) + '}' + '\n'*2 + subs
                    line = line.replace(match.group(0), replace_string)

            match_inp = re.compile(r"""\\inputdiagram{([^}]*)}""")
            for match in match_inp.finditer(line):
                subs = substitute_inputs(input_file_name(match.group(1)), directories)
                if subs:
                    replace_string = '\\small' + subs + '\\vspace{0.5cm}'
                    line = line.replace(match.group(0), replace_string)

            match_inp = re.compile(r"""\\input{([^}]*)}""")
            for match in match_inp.finditer(line):
                subs = substitute_inputs(input_file_name(match.group(1)), directories)
                if subs:
                    line = line.replace(match.group(0), subs)

            match_inp = re.compile(r"""\\includetalkfile{([^}]*)}""")
            for match in match_inp.finditer(line):
                subs = substitute_inputs(input_file_name(match.group(1)), directories)
                if subs:
                    line = line.replace(match.group(0), subs)

        new_lines += line

    
    return new_lines

def input_file_name(filename):
    if filename[-4:] == '.tex':
        return filename
    else:
        return filename + '.tex'

def process_tex_file(filename):
    tex_file_handle = open(filename, 'r')
    tex_file_lines = tex_file_handle.readlines()
    inp_list = extract_inputs(tex_file_lines)
    for inp in inp_list:
        if not inp[0] == '#':
            if inp[-4:] == '.tex':
                tex_file_lines += process_tex_file(inp)
            else:
                tex_file_lines += process_tex_file(inp + '.tex')
    return tex_file_lines

def extract_inputs(tex_file_lines):
    inp_list = []
    match_inp = re.compile(r"""\\newsection *{[^}]*} *{([^}]*)}""")
    for line in tex_file_lines.split('\n'):
        line_inp = match_inp.findall(line)
        if line_inp:
            for inp in line_inp:
                inp_list = inp_list + inp.split(',')

    match_inp = re.compile(r"""\\newsubsection *{[^}]*} *{([^}]*)}""")
    for line in tex_file_lines:
        line_inp = match_inp.findall(line)
        if line_inp:
            for inp in line_inp:
                inp_list = inp_list + inp.split(',')

    match_inp = re.compile(r"""\\includetalkfile{([^}]*)}""")
    for line in tex_file_lines:
        line_inp = match_inp.findall(line)
        if line_inp:
            for inp in line_inp:
                inp_list = inp_list + inp.split(',')

    match_inp = re.compile(r"""\\input *{([^}]*)}""")
    for line in tex_file_lines:
        line_inp = match_inp.findall(line)
        if line_inp:
            for inp in line_inp:
                inp_list = inp_list + inp.split(',')


    match_inp = re.compile(r"""\\input{([^}]*)}""")
    for line in tex_file_lines:
        line_inp = match_inp.findall(line)
        if line_inp:
            for inp in line_inp:
                inp_list = inp_list + inp.split(',')


    return inp_list

def extract_diagrams(tex_file_lines):
    diagram_list = []
    match_diagram = re.compile(r"""\\includegraphics *\[[^\]]*\] *{([^}]*)}""")
    for line in tex_file_lines.split('\n'):
        line_diagram = match_diagram.findall(line)
        if line_diagram:
            for diagram in line_diagram:
                diagram_list = diagram_list + diagram.split(',')

    match_diagram = re.compile(r"""\\includegraphics<[^>]*>{([^}]*)}""")
    for line in tex_file_lines.split('\n'):
        line_diagram = match_diagram.findall(line)
        if line_diagram:
            for diagram in line_diagram:
                diagram_list = diagram_list + diagram.split(',')

    match_diagram = re.compile(r"""\\includegraphics<[^>]*>\[[^\]]*\]{([^}]*)}""")
    for line in tex_file_lines:
        line_diagram = match_diagram.findall(line)
        if line_diagram:
            for diagram in line_diagram:
                diagram_list = diagram_list + diagram.split(',')

    match_diagram = re.compile(r"""\\includegraphics{([^}]*)}""")
    for line in tex_file_lines:
        line_diagram = match_diagram.findall(line)
        if line_diagram:
            for diagram in line_diagram:
                diagram_list = diagram_list + diagram.split(',')


    return diagram_list

def extract_citations(tex_file_lines):
     citations_list = []
     match_cite = re.compile(r"""\\cite[^\{]*{([^}\\#]+)}""")
     full_text = ''
     for line in tex_file_lines.split('\n'):
         full_text += line
     line_cite = match_cite.findall(full_text)
     if line_cite:
         for cite in line_cite:
             citations_list = citations_list + cite.split(',')
     for i in range(len(citations_list)):
         for j in range(i+1, len(citations_list)):
             if citations_list[i] == citations_list[j]:
                  citations_list[j] = [];

     return citations_list

def make_bib_file(citations_list, bib_files):

    if citations_list:
        citations_list.sort()
        cross_ref_list = []
        string_list = []
        out = ''
        # Get the location of the bibfiles
        bib_dir = os.environ['BIBINPUTS'].split(':')

        # Regular expressions 
        match_bib_field = re.compile(r"""(\@\w+{)""")
        match_cross_ref = re.compile(r"""\bcrossref\s*=\s*[\"|{](.*)[}|\"]""", re.i_g_n_o_r_e_c_a_s_e)
        match_string = re.compile(r"""\b\w*\s*=\s*(\w[^0-9]\w*),""")

        for dir in bib_dir:
            if not dir:
                dir = '.'
            for filename in bib_files:
                if os.access(os.path.join(dir, filename)+".bib", os.f__o_k):
                    bib_file_handle = open(os.path.join(dir, filename) + ".bib", 'r')
                    bib_file = bib_file_handle.read()
                    # Split the bib file at the entries.
                    bib_comp = match_bib_field.split(bib_file)
                    for i in range(len(citations_list)):
                        if citations_list[i]:
                            if i>0 and citations_list[i] == citations_list[i-1]:
                                citations_list[i] = []
                                continue
                            for j in range(2, len(bib_comp)):
                                entry = bib_comp[j].split(',')
                                entry = entry[0].split('=')
                                if not entry[0].find(citations_list[i])==-1:
                                    #print entry[0]
                                    # Adds the entry to output
                                    out = out + bib_comp[j-1] + bib_comp[j]
                                    # Removes the citation from the list
                                    citations_list[i] = []
                                    cross_refs = match_cross_ref.findall(bib_comp[j])
                                    if cross_refs:
                                        cross_ref_list = cross_ref_list + cross_refs
                                    else:                                        
                                        strings = match_string.findall(bib_comp[j])
                                        if strings:
                                            for string in strings:
                                                if not string_list.count(string):
                                                    string_list.append(string)
                                    break
        return get_bib_strings(string_list, bib_files) + out + get_bib_cross_refs(cross_ref_list, bib_files)
    else:
        return ''
    
def get_bib_strings(string_list, bib_files):
   if string_list:
       return make_bib_file(string_list, bib_files)
   else:
       return ''
      
def get_bib_cross_refs(string_list, bib_files):
   if string_list:
       return make_bib_file(string_list, bib_files)
   else:
       return ''


def create_bib_file_given_tex(tex_file_lines):

   bib_files = extract_bib_files(tex_file_lines)
   citations_list = extract_citations(tex_file_lines)

   return make_bib_file(citations_list, bib_files)

