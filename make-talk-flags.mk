DATE=$(shell date '+%Y-%m-%d')
MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_SVG"
CSS=talks.css
AUTHOR=[cat,dog]
HEADER=../svg-mathjax.html
PP=gpp
PPFLAGS=-T 
PPFLAGS=-I./..
PDFLAGS=--filter pandoc-citeproc --csl=../elsevier-harvard.csl --mathjax=${MATHJAX} 
PDSFLAGS=-s -S ${PDFLAGS}
SFLAGS=--slide-level 3 
