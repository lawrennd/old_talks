BASE=uncertainty-quantification
#BASE=deep-gaussian-processes
DATE=$(shell date '+%Y-%m-%d')
#DATE=2017-12-04
#MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_SVG"
CSS=talks.css
HEADER=../svg-mathjax.html
PP=gpp
PPFLAGS=-T 
PPFLAGS=-I./..
PDFLAGS=-s --slide-level 3 --filter pandoc-citeproc --csl=../elsevier-harvard.csl --mathjax=${MATHJAX} 
OUT=$(DATE)-$(BASE)

all: ${BASE}.slides.html ${BASE}.notes.html ${BASE}.ipynb

${BASE}.slides.html: ${BASE}.slides.md
	pandoc  ${PDFLAGS} -c ${CSS} --include-in-header=${HEADER} -t revealjs --bibliography=${BASE}.bib -o ${BASE}.slides.html  ${BASE}.slides.md 
	cp ${BASE}.slides.html ../slides/${OUT}.slides.html


${BASE}.notes.html: ${BASE}.notes.md
	pandoc  --bibliography=${BASE}.bib -o ${BASE}.notes.html  ${BASE}.notes.md 

${BASE}.ipynb: ${BASE}.ipynb.md
	pandoc  --bibliography=${BASE}.bib -o ${BASE}.tmp.md  ${BASE}.ipynb.md 
	notedown ${BASE}.tmp.md > ${BASE}.ipynb
	cp ${BASE}.ipynb ../notebooks/${OUT}.ipynb
	rm ${BASE}.tmp.md

${BASE}.slides.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" ${PPFLAGS} ${BASE}.md -o ${BASE}.slides.md

${BASE}.notes.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -Dnotes=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.notes.md

${BASE}.ipynb.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -Dipynb=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.ipynb.md

clean:
	rm ${BASE}.slides.md ${BASE}.slides.html ${BASE}.notes.md ${BASE}.notes.html ${BASE}.ipynb.md 
