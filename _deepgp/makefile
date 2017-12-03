BASE=deep-probabilistic-modelling-with-gaussian-processes
#BASE=deep-gaussian-processes
DATE=$(shell date '+%Y-%m-%d')
DATE=2017-12-04
#MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_SVG"
CSS=talks.css
HEADER=../svg-mathjax.html
PP=gpp
PPFLAGS=-T
PPFLAGS=
PDFLAGS=-s --slide-level 3 --filter pandoc-citeproc --csl=elsevier-harvard.csl --mathjax=${MATHJAX} 
OUT=$(DATE)-$(BASE)

all: ${BASE}.slides.html 

${BASE}.slides.html: ${BASE}.slides.md
	pandoc  ${PDFLAGS} -c ${CSS} --include-in-header=${HEADER} -t revealjs --bibliography=${BASE}.bib -o ${BASE}.slides.html  ${BASE}.slides.md 
	cp ${BASE}.slides.html ../slides/${OUT}.slides.html

${BASE}.slides.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" ${PPFLAGS} ${BASE}.md -o ${BASE}.slides.md

clean:
	rm ${BASE}.slides.md ${BASE}.slides.html 
