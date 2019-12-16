import os
import re
from datetime import date
import yaml
import _python.ndltex as latex


today = date.today()
defaults = {'categories': ['notes'],
            'date': today,
            'ipynb': False,
            'pptx': False,
            'docx': False,
            'pdf': False,
            'posts': True,
            'reveal': True,
            'slidesipynb': False,
            'notespdf': False,
            'potx': '../_includes/custom-reference.potx',
            'dotx': '../_includes/custom-reference.dotx'}

def header_fields(filename):
    """Extract headers from a talk file."""
    md= open(filename, 'r')
    text = md.read()
    md.close()
    match = re.findall('^---[\s\S]+?---', text)
    if match:
        # Strips `---` to create a valid yaml object
        ymd = match[0].replace('---', '')
        return yaml.load(ymd, Loader=yaml.FullLoader)
    md.close()

    raise OSError(1, "This does not appear to be a valid talk file.", filename)

def talk_field(field, filename):
    """Return one field from a talk."""
    fields = header_fields(filename)
    return header_field(field, fields)    


def header_field(field, fields):
    """Return one field from talk header fields."""
    if field not in fields:
        if field in defaults:
            answer=defaults[field]
        else:
            raise OSError(1, "Field not found in file or defaults.", filename)
    else:
        answer = fields[field]
    return answer
        
def extract_bibinputs(filename):
    """Extract bibinput files form a talk"""
    # Hard coded for the moment
    return ['../lawrence.bib', '../other.bib', '../zbooks.bib']

def extract_all(filename):
    """List the different files the talk file creates."""
    basename = os.path.basename(filename)
    base = os.path.splitext(basename)[0]
    fields = header_fields(filename)
    list_files = []
    if header_field('posts', fields):
        list_files += [base + '.posts.html']
    if header_field('ipynb', fields):
        list_files += [base + '.ipynb']
    if header_field('docx', fields):
        list_files += [base + '.docx']
    if header_field('notespdf', fields):
        list_files += [base + '.notes.pdf']
    if header_field('reveal', fields):
        list_files += [base + '.slides.html']
    if header_field('slidesipynb', fields):
        list_files += [base + '.slides.ipynb']
    if header_field('pptx', fields):
        list_files += [base + '.pptx']
        
    return list_files

def extract_inputs(filename):
    """Extract input files from a talk"""
    print(filename)
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
        else:
            not_present.append(filename)
                
    filenames = list_files
    
    for i, filename in enumerate(filenames):
        list_files[i+1:i+1] = extract_inputs(filename) 

    return list_files + not_present

def extract_diagrams(filename):
    """Extract diagrams from a talk"""
    filenames = [filename] + extract_inputs(filename)

    listdiagrams = []
    for filename in filenames:
        # exclude talk-macros file.
        if filename[:14] =='../talk-macros':
            continue

        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        for ext in ['png', 'jpg', 'gif']:
            diagrams = latex.extract_diagrams(lines, ext)
            diag_list = []
            for i, diag_str in enumerate(diagrams):
                if "\\" not in diag_str:
                    diag_list.append(diag_str + '.' + ext)
            listdiagrams.extend(diag_list)
        diagrams = latex.extract_diagrams(lines, 'diagram')
        png_list = []
        emf_list = []
        pdf_list = []
        diag_list = []
        for i, diag_str in enumerate(diagrams):
            if "\\" not in diag_str:
                diag_list.append(diag_str + '.svg')
                png_list.append(diag_str + '.png')
                emf_list.append(diag_str + '.emf')
                pdf_list.append(diag_str + '.pdf')

        listdiagrams.extend(diag_list)
        listdiagrams.extend(png_list)
        listdiagrams.extend(emf_list)
        listdiagrams.extend(pdf_list)

    full_list = []
    for diag in listdiagrams:
        full_list.append(os.path.abspath(diag))
    return full_list
