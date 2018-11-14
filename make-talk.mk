OUT=$(DATE)-$(BASE)

all: ${BASE}.slides.html ${BASE}.notes.html ${BASE}.posts.html ${BASE}.slides.ipynb ${BASE}.ipynb ${BASE}.notes.pdf 

${BASE}.slides.html: ${BASE}.slides.md
	printf '' > ../include.tmp
	printf '\[' >> ../include.tmp
	cat ../_includes/talk-notation.tex >> ../include.tmp
	printf '\]' >> ../include.tmp
	printf '' >> ../include.tmp
	#pandoc  --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.md 
	pandoc  -B ../include.tmp --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.md 
	cp ${BASE}.slides.html ../slides/${OUT}.slides.html
	rm ../include.tmp

${BASE}.notes.pdf: ${BASE}.notes.md
	pandoc  -B ../_includes/talk-notation.tex ${PDFLAGS} --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.notes.pdf  ${BASE}.notes.md 

${BASE}.notes.html: ${BASE}.notes.md
	pandoc  ${PDSFLAGS} --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.notes.html  ${BASE}.notes.md 

${BASE}.posts.html: ${BASE}.notes.md
	pandoc --template pandoc-jekyll-talk-template ${PDFLAGS} \
	       --atx-headers --metadata date=${DATE} \
               --metadata layout=talk \
               --metadata reveal=${OUT}.slides.html \
               --metadata ipynb=${OUT}.ipynb \
               --metadata published=${DATE} \
               --bibliography=../lawrence.bib \
               --bibliography=../other.bib \
               --bibliography=../zbooks.bib \
               --to html \
               --out ${BASE}.posts.html  ${BASE}.notes.md 
	cp ${BASE}.posts.html ../_posts/${OUT}.html


${BASE}.ipynb: ${BASE}.ipynb.md
	pandoc  ${PDFLAGS} -B ../_includes/talk-notation.tex --template pandoc-jekyll-ipynb-template --atx-headers --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.md  ${BASE}.ipynb.md
	notedown ${BASE}.tmp.md > ${BASE}.ipynb
	cp ${BASE}.ipynb ../_notebooks/${OUT}.ipynb
	rm ${BASE}.tmp.md

${BASE}.ipynb: ${BASE}.ipynb.md
	pandoc  ${PDFLAGS} -B ../_includes/talk-notation.tex --template pandoc-jekyll-ipynb-template --atx-headers --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.md  ${BASE}.ipynb.md
	notedown ${BASE}.tmp.md > ${BASE}.ipynb
	cp ${BASE}.ipynb ../_notebooks/${OUT}.ipynb
	rm ${BASE}.tmp.md

${BASE}.slides.ipynb: ${BASE}.slides.ipynb.md
	pandoc  ${PDFLAGS} -B ../_includes/talk-notation.tex --template pandoc-jekyll-ipynb-template --atx-headers --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.md  ${BASE}.slides.ipynb.md
	notedown ${BASE}.tmp.md > ${BASE}.slides.ipynb
	cp ${BASE}.slides.ipynb ../_notebooks/${OUT}.slides.ipynb
	rm ${BASE}.tmp.md


${BASE}.slides.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" ${PPFLAGS} ${BASE}.md -o ${BASE}.slides.md

${BASE}.notes.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -Dnotes=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.notes.md

${BASE}.ipynb.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -Dipynb=1 -Dnotes=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.ipynb.md

${BASE}.slides.ipynb.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -Dipynb=1 -Dslides=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.slides.ipynb.md


clean:
	rm ${BASE}.slides.md ${BASE}.slides.html ${BASE}.notes.md ${BASE}.notes.html ${BASE}.slides.ipynb.md ${BASE}.ipynb.md ${BASE}.posts.html
