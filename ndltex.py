#!/usr/bin/env python

import re
import os

tex_directories = os.environ['BIBINPUTS'].split(':') + os.environ['TEXINPUTS'].split(':')
def replaceNotation(texFileLines,
                    oldNotation,
                    newNotation):
    """Replace a given notation with a new notation"""
    #    openBracketList ='\(|\[|\{'
    #closeBracketList = '\)|\]|\}'
    #mathSymbol = '=|+|-\)|\]|\}'
    #subSuperList = '\^|_'
    #notationReg = '[' + openBracketList +'|'+ closeBracketList +'|' + subSuperList+'|'+ '\s' + oldNotation \^|_|\s|\]|\}|oldNotation
    filename = ''
    for line in texFileLines:
        filename = filename + line

    terminate = '[^\w|_]'
    startMath = re.escape('$')
    notReg = re.compile(r'([' + startMath + ']' + '[^' + startMath + ']*' + terminate + ')' + oldNotation + '(' + terminate + ')')
    matches = notReg.findall(filename)
    return matches

def extractBibFiles(texFileLines):
    """Extract the bib files from a tex file."""
    
    bibFiles = []
    matchBib = re.compile(r"""\\bibliography{([^}]*)}""")
    matchBib2 = re.compile(r"""\\begin{btSect}.*{([^}]*)}""")
    for line in texFileLines.split('\n'):
       lineBib = matchBib.findall(line)
       if lineBib:
           for bib in lineBib:
               bibFiles = bibFiles + bib.split(',')
       lineBib2 = matchBib2.findall(line)
       if lineBib2:
           for bib in lineBib2:
               bibFiles = bibFiles + bib.split(',')

    return bibFiles

def substituteInputs(filename, directories=None):
    
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
    texFileHandle = None
    for directory in directories:
        full_filename = os.path.join(directory, filename)
        if os.path.exists(full_filename):
            texFileHandle = open(full_filename, 'r')
            dirname = directory
            break
    if not texFileHandle:
        return None
    texFileLines = texFileHandle.readlines()
    newLines = ''
    # Avoid parsing defined commands in notation def.
    for line in texFileLines:
        if not line[0] == '%':
            matchInp = re.compile(r"""\\newsection *{([^}]*)} *{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(2)), directories)
                if subs:
                    replaceString = '\\section{' + match.group(1) + '}' + '\n'*2 + subs
                    line = line.replace(match.group(0), replaceString)

            matchInp = re.compile(r"""\\newsubsection *{([^}]*)} *{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(2)), directories)
                if subs:
                    replaceString = '\\subsection{' + match.group(1) + '}' + '\n'*2 + subs
                    line = line.replace(match.group(0), replaceString)

            matchInp = re.compile(r"""\\inputdiagram{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(1)), directories)
                if subs:
                    replaceString = '\\small' + subs + '\\vspace{0.5cm}'
                    line = line.replace(match.group(0), replaceString)

            matchInp = re.compile(r"""\\input{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(1)), directories)
                if subs:
                    line = line.replace(match.group(0), subs)

            matchInp = re.compile(r"""\\includetalkfile{([^}]*)}""")
            for match in matchInp.finditer(line):
                subs = substituteInputs(inputFileName(match.group(1)), directories)
                if subs:
                    line = line.replace(match.group(0), subs)

        newLines += line

    
    return newLines

def inputFileName(filename):
    if filename[-4:] == '.tex':
        return filename
    else:
        return filename + '.tex'

def processTexFile(filename):
    texFileHandle = open(filename, 'r')
    texFileLines = texFileHandle.readlines()
    inpList = extractInputs(texFileLines)
    for inp in inpList:
        if not inp[0] == '#':
            if inp[-4:] == '.tex':
                texFileLines += processTexFile(inp)
            else:
                texFileLines += processTexFile(inp + '.tex')
    return texFileLines

def extractInputs(texFileLines):
    inpList = []
    matchInp = re.compile(r"""\\newsection *{[^}]*} *{([^}]*)}""")
    for line in texFileLines.split('\n'):
        lineInp = matchInp.findall(line)
        if lineInp:
            for inp in lineInp:
                inpList = inpList + inp.split(',')

    matchInp = re.compile(r"""\\newsubsection *{[^}]*} *{([^}]*)}""")
    for line in texFileLines:
        lineInp = matchInp.findall(line)
        if lineInp:
            for inp in lineInp:
                inpList = inpList + inp.split(',')

    matchInp = re.compile(r"""\\includetalkfile{([^}]*)}""")
    for line in texFileLines:
        lineInp = matchInp.findall(line)
        if lineInp:
            for inp in lineInp:
                inpList = inpList + inp.split(',')

    matchInp = re.compile(r"""\\input *{([^}]*)}""")
    for line in texFileLines:
        lineInp = matchInp.findall(line)
        if lineInp:
            for inp in lineInp:
                inpList = inpList + inp.split(',')


    matchInp = re.compile(r"""\\input{([^}]*)}""")
    for line in texFileLines:
        lineInp = matchInp.findall(line)
        if lineInp:
            for inp in lineInp:
                inpList = inpList + inp.split(',')


    return inpList

def extractDiagrams(texFileLines):
    diagramList = []
    matchDiagram = re.compile(r"""\\includegraphics *\[[^\]]*\] *{([^}]*)}""")
    for line in texFileLines.split('\n'):
        lineDiagram = matchDiagram.findall(line)
        if lineDiagram:
            for diagram in lineDiagram:
                diagramList = diagramList + diagram.split(',')

    matchDiagram = re.compile(r"""\\includegraphics<[^>]*>{([^}]*)}""")
    for line in texFileLines.split('\n'):
        lineDiagram = matchDiagram.findall(line)
        if lineDiagram:
            for diagram in lineDiagram:
                diagramList = diagramList + diagram.split(',')

    matchDiagram = re.compile(r"""\\includegraphics<[^>]*>\[[^\]]*\]{([^}]*)}""")
    for line in texFileLines:
        lineDiagram = matchDiagram.findall(line)
        if lineDiagram:
            for diagram in lineDiagram:
                diagramList = diagramList + diagram.split(',')

    matchDiagram = re.compile(r"""\\includegraphics{([^}]*)}""")
    for line in texFileLines:
        lineDiagram = matchDiagram.findall(line)
        if lineDiagram:
            for diagram in lineDiagram:
                diagramList = diagramList + diagram.split(',')


    return diagramList

def extractCitations(texFileLines):
    """Extract the citations from the given tex file lines"""
    citationsList = []
    matchCite = re.compile(r"""\\cite[^\{]*{([^}\\#]+)}""")
    fullText = ''
    for line in texFileLines.split('\n'):
        fullText += line
    lineCite = matchCite.findall(fullText)
    if lineCite:
        for cite in lineCite:
            citationsList = citationsList + cite.split(',')
    for i in range(len(citationsList)):
        for j in range(i+1, len(citationsList)):
            if citationsList[i] == citationsList[j]:
                citationsList[j] = [];

    return citationsList

def makeBibFile(citationsList, bibFiles):
    """Make a new bib file for the tex file."""
    if citationsList:
        citationsList.sort()
        crossRefList = []
        stringList = []
        out = ''
        # Get the location of the bibfiles
        bibDir = os.environ['BIBINPUTS'].split(':')

        # Regular expressions 
        matchBibField = re.compile(r"""(\@\w+{)""")
        matchCrossRef = re.compile(r"""\bcrossref\s*=\s*[\"|{](.*)[}|\"]""", re.IGNORECASE)
        matchString = re.compile(r"""\b\w*\s*=\s*(\w[^0-9]\w*),""")

        for dir in bibDir:
            if not dir:
                dir = '.'
            for filename in bibFiles:
                if os.access(os.path.join(dir, filename)+".bib", os.F_OK):
                    bibFileHandle = open(os.path.join(dir, filename) + ".bib", 'r')
                    bibFile = bibFileHandle.read()
                    # Split the bib file at the entries.
                    bibComp = matchBibField.split(bibFile)
                    for i in range(len(citationsList)):
                        if citationsList[i]:
                            if i>0 and citationsList[i] == citationsList[i-1]:
                                citationsList[i] = []
                                continue
                            for j in range(2, len(bibComp)):
                                entry = bibComp[j].split(',')
                                entry = entry[0].split('=')
                                if not entry[0].find(citationsList[i])==-1:
                                    #print(entry[0])
                                    # Adds the entry to output
                                    out = out + bibComp[j-1] + bibComp[j]
                                    # Removes the citation from the list
                                    citationsList[i] = []
                                    crossRefs = matchCrossRef.findall(bibComp[j])
                                    if crossRefs:
                                        crossRefList = crossRefList + crossRefs
                                    else:                                        
                                        strings = matchString.findall(bibComp[j])
                                        if strings:
                                            for string in strings:
                                                if not stringList.count(string):
                                                    stringList.append(string)
                                    break
        return getBibStrings(stringList, bibFiles) + out + getBibCrossRefs(crossRefList, bibFiles)
    else:
        return ''
    
def getBibStrings(stringList, bibFiles):
    if stringList:
        return makeBibFile(stringList, bibFiles)
    else:
        return ''
      
def getBibCrossRefs(stringList, bibFiles):
    if stringList:
        return makeBibFile(stringList, bibFiles)
    else:
        return ''


def createBibFileGivenTex(texFileLines):
    
    bibFiles = extractBibFiles(texFileLines)
    citationsList = extractCitations(texFileLines)

    return makeBibFile(citationsList, bibFiles)
