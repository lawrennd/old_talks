import os
from datetime import date

import _python.ndltex as latex
import _python.ndlyaml as ny


today = date.today()

# Update default values.
ny.defaults = {'slidedir': '../slides/',
            'notedir': '../_notes/',
            'notebookdir': '../_notebooks/',
            'postdir': '../_posts/',
            'talkcss': 'talks.css',
            'slidesheader': '../slides-header.html',
            'postsheader': '../posts-header.html',
            'week': 0,
            'categories': ['notes'],
            'ipynb': False,
            'pptx': False,
            'docx': False,
            'pdf': False,
            'posts': True,
            'reveal': True,
            'assignment': False,
            'slidesipynb': False,
            'notespdf': False,
            'potx': '../_includes/custom-reference.potx',
            'dotx': '../_includes/custom-reference.dotx'}

# Load defaults from config file if it exists.
default_file = '_config.yml'
if os.path.isfile(default_file):
    ny.defaults = ny.update_from_file(ny.defaults, default_file)
    

def talk_field(field, filename):
    """Return one field from a talk."""
    fields = ny.header_fields(filename)
    return ny.header_field(field, fields)    
        
def extract_bibinputs(filename):
    """Extract bibinput files form a talk"""
    # Hard coded for the moment
    return ['../lawrence.bib', '../other.bib', '../zbooks.bib']

def extract_all(filename):
    """List the different files the talk file creates."""
    basename = os.path.basename(filename)
    base = os.path.splitext(basename)[0]
    fields = ny.header_fields(filename)
    list_files = []
    if ny.header_field('posts', fields):
        list_files += [base + '.posts.html']
    if ny.header_field('ipynb', fields):
        list_files += [base + '.ipynb']
    if ny.header_field('docx', fields):
        list_files += [base + '.docx']
    if ny.header_field('notespdf', fields):
        list_files += [base + '.notes.pdf']
    if ny.header_field('reveal', fields):
        list_files += [base + '.slides.html']
    if ny.header_field('slidesipynb', fields):
        list_files += [base + '.slides.ipynb']
    if ny.header_field('pptx', fields):
        list_files += [base + '.pptx']
        
    return list_files

def extract_inputs(filename):
    """Extract input files from a talk"""
    if filename=='\\filename.svg':
        return []
    elif not os.path.exists(filename):
        print("Warning the file {} does not exist.".format(filename))
        return []
    else:

        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        filenames = latex.extract_inputs(lines)
        list_files=[]
        not_present=[]
        for i, filename in enumerate(filenames):
            includepos = os.path.join('../', filename)
            if os.path.isfile(filename):
                list_files.append(filename)
            elif os.path.isfile(includepos):
                list_files.append(includepos)
            elif filename == '\\filename.svg':
                pass
            else:
                not_present.append(filename)

        filenames = list_files

        for i, filename in enumerate(filenames):
            list_files[i+1:i+1] = extract_inputs(filename) 

        return list_files + not_present

def extract_diagrams(filename, absolute_path=True, diagram_exts=['svg', 'png', 'emf', 'pdf'], diagrams_dir=None):
    """Extract diagrams from a talk"""
    if os.path.exists(filename):
        filenames = [filename] + extract_inputs(filename)
    else:
        print("Warning, input file {} doesn't exist.".format(filename))
        return

    listdiagrams = []
    for filen in filenames:
        # exclude talk-macros file.
        if filen[:14] =='../talk-macros':
            continue

        if filen == '\\filename.svg':
            continue
        else:
            f = open(filen, 'r')
            lines = f.readlines()
            f.close()

        for ext in ['png', 'jpg', 'gif']:
            diagrams = latex.extract_diagrams(lines, ext)
            diag_list = []
            for i, diag_str in enumerate(diagrams):
                if diagrams_dir is not None: # Substitute if diagrams_dir exists
                    diag_str = diag_str.replace('\\diagramsDir', diagrams_dir)
                if "\\" not in diag_str: # Ignore remaining tex macros
                    diag_list.append(diag_str + '.' + ext)
            listdiagrams.extend(diag_list)
        diagrams = latex.extract_diagrams(lines, 'diagram')
        diag_dict = {}
        for ext in diagram_exts:
            diag_dict[ext] = []
        for i, diag_str in enumerate(diagrams):
            if diagrams_dir is not None: # Substitute if diagrams_dir exists
                diag_str = diag_str.replace('\\diagramsDir', diagrams_dir)
            if "\\" not in diag_str: # Ignore remaining tex macros
                for ext in diagram_exts:
                     diag_dict[ext].append(diag_str + '.' + ext)

        for ext in diagram_exts:
            listdiagrams.extend(diag_dict[ext])

    full_list = []
    if absolute_path:
        for diag in listdiagrams:
            full_list.append(os.path.abspath(diag))
    else:
        for diag in listdiagrams:
            full_list.append(diag)
    return full_list
