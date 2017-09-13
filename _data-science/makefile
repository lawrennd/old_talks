BASE=data-science-time-for-professionalisation
MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
CSS=tech-talks.css
PP=gpp
PPFLAGS=-T
PDFLAGS=-s -S --slide-level 3 --filter pandoc-citeproc --mathjax=${MATHJAX}
DATE=$(shell date '+%Y-%m-%d')
DATE=2017-10-13
OUT=$(DATE)-$(BASE)

all: ${BASE}.slides.html 

${BASE}.slides.html: ${BASE}.slides.md
	pandoc ${PDFLAGS} -c ${CSS} -t revealjs -o ${BASE}.slides.html  ${BASE}.slides.md 
	cp ${BASE}.slides.html ../slides/${OUT}.slides.html

${BASE}.slides.md: ${BASE}.md 
	${PP} ${PPFLAGS} ${BASE}.md -o ${BASE}.slides.md



clean:
	rm ${BASE}.slides.md ${BASE}.slides.html 
