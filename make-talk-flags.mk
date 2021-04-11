# This file checks the header of the base file for information about how to produce the talk and stores it in relevant files.

# Extract the date and the prefix of the produced files.
DATE=$(shell talkfield date ${BASE}.md)

CATEGORIES=$(shell talkfield categories ${BASE}.md)

MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_SVG"
REVEALJS="https://inverseprobability.com/talks/slides/reveal.js/"

SLIDESHEADER=$(shell talkfield slidesheader ${BASE}.md)
POSTSHEADER=$(shell talkfield postssheader ${BASE}.md)
ASSIGNMENT=$(shell talkfield assignment ${BASE}.md)
NOTATION=$(shell talkfield notation ${BASE}.md)

PREFIX=$(shell flags prefix ${BASE})

# Local calls for the preprocessor and inkscape
INKSCAPE=inkscape #/Applications/Inkscape.app/Contents/Resources/bin/inkscape
PP=mdpp

PPFLAGS=-T 
PPFLAGS=$(shell flags pp $(BASE))

BIBFLAGS=--bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib 

CITEFLAGS=--citeproc --csl=../elsevier-harvard.csl ${BIBFLAGS}

PDSFLAGS=-s ${CITEFLAGS} --mathjax=${MATHJAX} 

POSTDIR=$(shell talkfield postdir $(BASE).md)
NOTEDIR=$(shell talkfield notedir $(BASE).md)
NOTEBOOKDIR=$(shell talkfield notebookdir $(BASE).md)
SLIDEDIR=$(shell talkfield slidedir $(BASE).md)
WEEK=$(shell talkfield week $(BASE).md)
SESSION=$(shell talkfield session $(BASE).md)



DEPS=$(shell dependencies inputs $(BASE).md)
DIAGDEPS=$(shell dependencies diagrams $(BASE).md)
BIBDEPS=$(shell dependencies bibinputs $(BASE).md)

POSTFLAGS=$(shell flags post $(BASE))
PPTXFLAGS=$(shell flags pptx $(BASE))
DOCXFLAGS=$(shell flags docx $(BASE))
SFLAGS=$(shell flags reveal $(BASE))


ALL=$(shell dependencies all $(BASE).md)
