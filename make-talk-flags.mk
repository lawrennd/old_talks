# This file checks the header of the base file for information about how to produce the talk and stores it in relevant files.

# Extract the date and the prefix of the produced files.
DATE=$(shell mdfield date ${BASE}.md)

CATEGORIES=$(shell mdfield categories ${BASE}.md)

MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_SVG"
REVEALJS="https://inverseprobability.com/talks/slides/reveal.js/"

SLIDESHEADER=$(shell mdfield slidesheader ${BASE}.md)
POSTSHEADER=$(shell mdfield postssheader ${BASE}.md)
ASSIGNMENT=$(shell mdfield assignment ${BASE}.md)
NOTATION=$(shell mdfield notation ${BASE}.md)

PREFIX=$(shell flags prefix ${BASE})

# Local calls for the preprocessor and inkscape
INKSCAPE=/Applications/Inkscape.app/Contents/MacOS/inkscape
PP=mdpp

PPFLAGS=-T 
PPFLAGS=$(shell flags pp $(BASE))

BIBFLAGS=--bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib 

CITEFLAGS=--citeproc --csl=../elsevier-harvard.csl ${BIBFLAGS}

PDSFLAGS=-s ${CITEFLAGS} --mathjax=${MATHJAX} 

DIAGRAMSDIR=$(shell mdfield diagramsdir $(BASE).md)
WRITEDIAGRAMSDIR=$(shell mdfield writediagramsdir $(BASE).md)
POSTSDIR=$(shell mdfield postsdir $(BASE).md)
NOTESDIR=$(shell mdfield notesdir $(BASE).md)
NOTEBOOKSDIR=$(shell mdfield notebooksdir $(BASE).md)
SLIDESDIR=$(shell mdfield slidesdir $(BASE).md)
TEXDIR=$(shell mdfield texdir $(BASE).md)
WEEK=$(shell mdfield week $(BASE).md)
SESSION=$(shell mdfield session $(BASE).md)



DEPS=$(shell dependencies inputs $(BASE).md)
DIAGDEPS=$(shell dependencies diagrams $(BASE).md)
BIBDEPS=$(shell dependencies bibinputs $(BASE).md)
DOCXDEPS=$(shell dependencies docxdiagrams $(BASE).md)
TEXDEPS=$(shell dependencies texdiagrams $(BASE).md)

POSTFLAGS=$(shell flags post $(BASE))
PPTXFLAGS=$(shell flags pptx $(BASE))
DOCXFLAGS=$(shell flags docx $(BASE))
SLIDEFLAGS=$(shell flags reveal $(BASE))


ALL=$(shell dependencies all $(BASE).md)
