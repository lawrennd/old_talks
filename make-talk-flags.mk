DATE=$(shell ../talkfield.py date ${BASE}.md)
CATEGORIES=$(shell ../talkfield.py categories ${BASE}.md)
MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_SVG"
CSS=talks.css
SLIDESHEADER=../slides-header.html
POSTSHEADER=../posts-header.html
PP=gpp
PPFLAGS=-T 
PPFLAGS=-I./..
BIBFLAGS=--bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib 
CITEFLAGS=--filter pandoc-citeproc --csl=../elsevier-harvard.csl ${BIBFLAGS}
PDSFLAGS=-s ${CITEFLAGS} --mathjax=${MATHJAX} 
SFLAGS=--slide-level 3
INKSCAPE=inkscape #/Applications/Inkscape.app/Contents/Resources/bin/inkscape
