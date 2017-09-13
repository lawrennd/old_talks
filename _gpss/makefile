BASE=gpss-session-
MATHJAX="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
CSS=tech-talks.css
PP=gpp
PPFLAGS=-T
PDFLAGS=-s -S --slide-level 3 --filter pandoc-citeproc --mathjax=${MATHJAX}
DATE1=$(shell date '+%Y-%m-%d')
DATE1=2017-09-11
DATE2=2017-09-12
OUT1=$(DATE1)-$(BASE)1
OUT2=$(DATE2)-$(BASE)2


${BASE}1.slides.html: ${BASE}1.slides.md
	pandoc ${PDFLAGS} -c ${CSS} -t revealjs -o ${BASE}1.slides.html  ${BASE}1.slides.md 
	cp ${BASE}1.slides.html ../slides/${OUT1}.slides.html

${BASE}2.slides.html: ${BASE}2.slides.md
	pandoc ${PDFLAGS} -c ${CSS} -t revealjs -o ${BASE}2.slides.html  ${BASE}2.slides.md 
	cp ${BASE}2.slides.html ../slides/${OUT2}.slides.html

${BASE}1.slides.md: ${BASE}1.md 
	${PP} ${PPFLAGS} ${BASE}1.md -o ${BASE}1.slides.md

${BASE}2.slides.md: ${BASE}2.md
	${PP} ${PPFLAGS} ${BASE}2.md -o ${BASE}2.slides.md


all: ${BASE}1.slides.html ${BASE}2.slides.html

clean:
	rm ${BASE}1.slides.md ${BASE}1.slides.html ${BASE}2.slides.html ${BASE}2.slides.md
