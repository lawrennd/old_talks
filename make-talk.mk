OUT=$(DATE)-$(BASE)

all: ${BASE}.slides.html ${BASE}.notes.html ${BASE}.posts.html ${BASE}.slides.ipynb ${BASE}.ipynb ${BASE}.notes.docx

##${BASE}.notes.tex ${BASE}.notes.pdf 

${BASE}.slides.html: ${BASE}.slides.html.md
	printf '' > ../include.tmp
	printf '\[' >> ../include.tmp
	cat ../_includes/talk-notation.tex >> ../include.tmp
	printf '\]' >> ../include.tmp
	printf '' >> ../include.tmp
	#pandoc  --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.html.md 
	pandoc  -B ../include.tmp --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.html.md 
	cp ${BASE}.slides.html ../slides/${OUT}.slides.html
	rm ../include.tmp


${BASE}.notes.pdf: ${BASE}.notes.aux ${BASE}.notes.bbl ${BASE}.notes.tex
	pdflatex -shell-escape ${BASE}.notes.tex
	cp ${BASE}.notes.pdf ../_notes/${OUT}.notes.pdf

${BASE}.notes.bbl: ${BASE}.notes.aux
	bibtex ${BASE}.notes

${BASE}.notes.aux: ${BASE}.notes.tex
	pdflatex -shell-escape ${BASE}.notes.tex


${BASE}.notes.tex: ${BASE}.notes.tex.md
	pandoc  -s -S \
		--template pandoc-notes-tex-template.tex \
		--number-sections \
		--natbib \
		${BIBFLAGS} \
		-B ../_includes/talk-notation.tex \
		-o ${BASE}.notes.tex  \
		${BASE}.notes.tex.md 

${BASE}.notes.docx: ${BASE}.notes.docx.md
	pandoc  ${CITEFLAGS} \
		--to docx \
		--out ${BASE}.notes.docx  \
		${BASE}.notes.docx.md 

${BASE}.notes.html: ${BASE}.notes.html.md
	pandoc  ${PDSFLAGS} \
		-o ${BASE}.notes.html  \
		${BASE}.notes.html.md 

${BASE}.posts.html: ${BASE}.notes.html.md
	pandoc --template pandoc-jekyll-talk-template ${PDFLAGS} \
	       --atx-headers \
	       --metadata date=${DATE} \
               --metadata layout=talk \
               --metadata reveal=${OUT}.slides.html \
               --metadata ipynb=${OUT}.ipynb \
               --metadata pdf=${OUT}.notes.pdf \
               --metadata published=${DATE} \
               --bibliography=../lawrence.bib \
               --bibliography=../other.bib \
               --bibliography=../zbooks.bib \
               --to html \
               --out ${BASE}.posts.html  ${BASE}.notes.html.md 
	cp ${BASE}.posts.html ../_posts/${OUT}.html


${BASE}.ipynb: ${BASE}.notes.ipynb.md
	pandoc  ${PDFLAGS} -B ../_includes/talk-notation.tex --template pandoc-jekyll-ipynb-template --atx-headers --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.md  ${BASE}.notes.ipynb.md
	notedown ${BASE}.tmp.md > ${BASE}.ipynb
	cp ${BASE}.ipynb ../_notebooks/${OUT}.ipynb
	rm ${BASE}.tmp.md

${BASE}.slides.ipynb: ${BASE}.slides.ipynb.md
	pandoc  ${PDFLAGS} -B ../_includes/talk-notation.tex --template pandoc-jekyll-ipynb-template --atx-headers --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.md  ${BASE}.slides.ipynb.md
	notedown ${BASE}.tmp.md > ${BASE}.slides.ipynb
	cp ${BASE}.slides.ipynb ../_notebooks/${OUT}.slides.ipynb
	rm ${BASE}.tmp.md


${BASE}.slides.html.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DHTML=1 -DSLIDES=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.slides.html.md

${BASE}.notes.html.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DNOTES=1 -DHTML=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.notes.html.md

${BASE}.notes.tex.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DNOTES=1 -DTEX=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.notes.tex.md
	# Fix percentage width for latex.
	sed -i -e 's/width=\(.*\)\%/width=0.\1\\textwidth/g' ${BASE}.notes.tex.md
	sed -i -e 's/width=\(.*\)\%/height=0.\1\\textheight/g' ${BASE}.notes.tex.md

${BASE}.notes.docx.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DNOTES=1 -DDOCX=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.notes.docx.md

${BASE}.notes.ipynb.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DIPYNB=1 -DNOTES=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.notes.ipynb.md

${BASE}.slides.ipynb.md: ${BASE}.md 
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DIPYNB=1 -DSLIDES=1 ${PPFLAGS} ${BASE}.md -o ${BASE}.slides.ipynb.md

clean:
	rm ${BASE}.slides.html.md \
		${BASE}.slides.html \
		${BASE}.notes.docx.md \
		${BASE}.notes.docx \
		${BASE}.notes.tex.md \
		${BASE}.notes.tex \
		${BASE}.notes.out \
		${BASE}.notes.log \
		${BASE}.notes.bbl \
		${BASE}.notes.aux \
		${BASE}.notes.html.md \
		${BASE}.notes.html \
		${BASE}.posts.html \
		${BASE}.ipynb \
		${BASE}.slides.ipynb.md \
		${BASE}.slides.ipynb
