OUT=$(DATE)-$(BASE)

all: ${BASE}.slides.html ${BASE}.notes.html ${BASE}.posts.html ${BASE}.ipynb 

${BASE}.slides.html: ${BASE}.slides.md
	pandoc  --template pandoc-revealjs-template ${PDFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=${HEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.md 
	cp ${BASE}.slides.html ../slides/${OUT}.slides.html

${BASE}.notes.pdf: ${BASE}.notes.md
	pandoc  ${PDFLAGS} --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.notes.pdf  ${BASE}.notes.md 

${BASE}.notes.html: ${BASE}.notes.md
	pandoc  ${PDFLAGS} --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.notes.html  ${BASE}.notes.md 

${BASE}.posts.html: ${BASE}.notes.md
	pandoc  --template pandoc-jekyll-talk-template ${PDFLAGS} --atx-headers --metadata date=${DATE} --metadata layout=talk --metadata reveal=${OUT}.slides.html --metadata published=${DATE} -t html --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.posts.html  ${BASE}.notes.md 
	cp ${BASE}.posts.html ../_posts/${OUT}.html

${BASE}.ipynb: ${BASE}.ipynb.md
	pandoc  ${PDFLAGS} --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.md  ${BASE}.ipynb.md 
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
	rm ${BASE}.slides.md ${BASE}.slides.html ${BASE}.notes.md ${BASE}.notes.html ${BASE}.ipynb.md ${BASE}.posts.html
