#!/usr/bin/env python

import re
import os

tex_directories = os.environ['BIBINPUTS'].split(':') + os.environ['TEXINPUTS'].split(':')

def replace_notation(lines, old_notation, new_notation):
    #    open_bracket_list ='\(|\[|\{'
    #close_bracket_list = '\)|\]|\}'
    #math_symbol = '=|+|-\)|\]|\}'
    #sub_super_list = '\^|_'
    #notation_reg = '[' + open_bracketList +'|'+ close_bracket_list +'|' + sub_super_list+'|'+ '\s' + old_notation \^|_|\s|\]|\}|old_notation
    filename = ''
    for line in lines:
        filename = filename + line

    terminate = '[^\w|_]'
    start_math = re.escape('$')
    not_reg = re.compile(r'([' + start_math + ']' + '[^' + start_math + ']*' + terminate + ')' + old_notation + '(' + terminate + ')')
    matches = not_reg.findall(filename)
    return matches

def extract_bib_files(lines):
    bib_files = []
    match_bib = re.compile(r"""\\bibliography{([^}]*)}""")
    match_bib2 = re.compile(r"""\\begin{btSect}.*{([^}]*)}""")
    for line in lines:
       line_bib = match_bib.findall(line)
       if line_bib:
           for bib in line_bib:
               bib_files = bib_files + bib.split(',')
       line_bib2 = match_bib2.findall(line)
       if line_bib2:
           for bib in line_bib2:
               bib_files = bib_files + bib.split(',')

    return bib_files

def substitute_inputs(filename, directories=None):
    """Take the base file and substitute in any input and include files."""
    print(filename)
    file_dir = os.path.dirname(filename)
    if directories == None:
        directories = [file_dir]
        filename = os.path.basename(filename)
    elif len(file_dir)>0:
        if file_dir not in directories:
            directories.append(file_dir)

    for directory in tex_directories:
        if directory not in directories:
            directories.append(directory)
    if filename[0] == '#': # it's a macro
        return None
    tex_file_handle = None
    for directory in directories:
        full_filename = os.path.join(directory, filename)
        if os.path.exists(full_filename):
            tex_file_handle = open(full_filename, 'r')
            dirname = directory
            break
    if not tex_file_handle:
        return None
    lines = tex_file_handle.readlines()
    new_lines = ''
    # Avoid parsing defined commands in notation def.
    for line in lines:
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

            match_inp = re.compile(r"""\\include{([^}]*)}""")
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

def input_file_name(filename, extension='.tex'):
    ext_list = ['md', 'tex']
    if os.path.exists(filename):
        return filename
    else:
        for ext in ext_list:
            if os.path.exists(filename + '.' + ext):
                return filename + '.' + ext

def process_file(filename, extension='.tex'):
    tex_file_handle = open(filename, 'r')
    lines = tex_file_handle.readlines()
    inp_list = extract_inputs(lines)
    for inp in inp_list:
        if not inp[0] == '#':
            if inp[-len(extension):] == extension:
                lines += process_file(inp, extension)
            else:
                lines += process_file(inp + extension, extension)
    return lines

def extract_inputs(lines):
    """Extract latex file dependencies."""
    def extract_input(lines, matchstr):
        inp_list = []
        for line in lines:
            line_inp = re.compile(matchstr).findall(line)
            if line_inp:
                for inp in line_inp:
                    inp_list = inp_list + inp.split(',')
        return inp_list
    inp_list = []
    inp_list += extract_input(lines,
                              r"""\\newsection *{[^}]*} *{([^}]*)}""")
    inp_list += extract_input(lines,
                              r"""\\newsubsection *{[^}]*} *{([^}]*)}""")
    inp_list += extract_input(lines,
                              r"""\\includetalkfile{([^}]*)}""")
    inp_list += extract_input(lines,
                              r"""\\input *{([^}]*)}""")
    inp_list += extract_input(lines,
                              r"""\\include *{([^}]*)}""")
    inp_list += extract_input(lines,
                              r"""\\input{([^}]*)}""")
    return inp_list

def extract_diagrams(lines, type='all'):
    """Extract all the diagrams listed in the file."""
    diagram_list = []

    rebases={}
    rebases['diagram'] = [r'\\includediagram',
                          r'\\includediagramclass',
                          r'\\inlinediagram']
    rebases['img'] = [r'\\includeimg']
    rebases['png'] = [r'\\includepng']
    rebases['gif'] = [r'\\includegif']
    rebases['jpg'] = [r'\\includejpg']
    all_val = []
    for key in rebases:
        all_val += rebases[key]
    rebases['all'] = all_val
        
    retails = [r" *\[[^\]]*\] *{([^}]*)}",
                r"<[^>]*>{([^}]*)}",
                r"<[^>]*>\[[^\]]*\]{([^}]*)}",
                r"{([^}]*)}"]
    for rebase in rebases[type]:
        for retail in retails:
            match_diagram = re.compile(rebase + retail)
            for line in lines:
                line_diagram = match_diagram.findall(line)
                if line_diagram:
                    for diagram in line_diagram:
                        diagram_list += diagram.split(',')

    return diagram_list


def extract_citations(lines):
     """Extract all the citations listed in the file lines."""
     citations_list = []
     match_cite = re.compile(r"""\\cite[^\{]*{([^}\\#]+)}""")
     full_text = ''
     for line in lines:
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


def create_bib_file_given_tex(lines):
    """Create a new bibliography file for a given latex file."""
    bib_files = extract_bib_files(lines)
    citations_list = extract_citations(lines)

    return make_bib_file(citations_list, bib_files)

