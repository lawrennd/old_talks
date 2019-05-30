
OUT=$(DATE)-$(BASE)
DEPS=$(shell ../makedependency_talk.py $(BASE).md)
DIAGDEPS=$(shell ../makediagdependency_talk.py $(BASE).md)
BIBDEPS=../lawrence.bib ../other.bib ../zbooks.bib

all: ${BASE}.slides.html ${BASE}.notes.html ${BASE}.posts.html ${BASE}.slides.ipynb ${BASE}.ipynb ${BASE}.notes.docx ${BASE}.notes.pdf

##${BASE}.notes.tex ${BASE}.notes.pdf 

${BASE}.slides.html: ${BASE}.slides.html.markdown ${BIBDEPS}
	printf '' > ../include.tmp
	printf '\[' >> ../include.tmp
	cat ../_includes/talk-notation.tex >> ../include.tmp
	printf '\]' >> ../include.tmp
	printf '' >> ../include.tmp
	#pandoc  --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.html.markdown 
	pandoc  -B ../include.tmp --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.html.markdown 
	cp ${BASE}.slides.html ../slides/${OUT}.slides.html
	rm ../include.tmp


${BASE}.notes.pdf: ${BASE}.notes.aux ${BASE}.notes.bbl ${BASE}.notes.tex
	pdflatex -shell-escape ${BASE}.notes.tex
	cp ${BASE}.notes.pdf ../_notes/${OUT}.notes.pdf

${BASE}.notes.bbl: ${BASE}.notes.aux ${BIBDEPS}
	bibtex ${BASE}.notes

${BASE}.notes.aux: ${BASE}.notes.tex
	pdflatex -shell-escape ${BASE}.notes.tex


${BASE}.notes.tex: ${BASE}.notes.tex.markdown 
	pandoc  -s \
		--template pandoc-notes-tex-template.tex \
		--number-sections \
		--natbib \
		${BIBFLAGS} \
		-B ../_includes/talk-notation.tex \
		-o ${BASE}.notes.tex  \
		${BASE}.notes.tex.markdown 

${BASE}.notes.docx: ${BASE}.notes.docx.markdown ${BIBDEPS} ${DIAGDEPS}
	pandoc  ${CITEFLAGS} \
		--to docx \
		--out ${BASE}.notes.docx  \
		${BASE}.notes.docx.markdown 

${BASE}.notes.html: ${BASE}.notes.html.markdown ${BIBDEPS}
	pandoc  ${PDSFLAGS} \
		-o ${BASE}.notes.html  \
		${BASE}.notes.html.markdown 

${BASE}.posts.html: ${BASE}.notes.html.markdown
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
               --out ${BASE}.posts.html  ${BASE}.notes.html.markdown 
	cp ${BASE}.posts.html ../_posts/${OUT}.html


${BASE}.ipynb: ${BASE}.notes.ipynb.markdown
	pandoc  ${PDFLAGS} -B ../_includes/talk-notation.tex --template pandoc-jekyll-ipynb-template --atx-headers --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.markdown  ${BASE}.notes.ipynb.markdown
	notedown ${BASE}.tmp.markdown > ${BASE}.ipynb
	cp ${BASE}.ipynb ../_notebooks/${OUT}.ipynb
	rm ${BASE}.tmp.markdown

${BASE}.slides.ipynb: ${BASE}.slides.ipynb.markdown
	pandoc  ${PDFLAGS} -B ../_includes/talk-notation.tex --template pandoc-jekyll-ipynb-template --atx-headers --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.tmp.markdown  ${BASE}.slides.ipynb.markdown
	notedown ${BASE}.tmp.markdown > ${BASE}.slides.ipynb
	cp ${BASE}.slides.ipynb ../_notebooks/${OUT}.slides.ipynb
	rm ${BASE}.tmp.markdown


${BASE}.slides.html.markdown: ${BASE}.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DHTML=1 -DSLIDES=1 ${PPFLAGS} $< -o $@  

%.notes.html.markdown: %.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DNOTES=1 -DHTML=1 ${PPFLAGS} $< -o $@

%.notes.tex.markdown: %.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DNOTES=1 -DTEX=1 ${PPFLAGS} $< -o $@
	# Fix percentage width for latex.
	sed -i -e 's/width=\(.*\)\%/width=0.\1\\textwidth/g' $@
	sed -i -e 's/height=\(.*\)\%/height=0.\1\\textheight/g' $@

%.notes.docx.markdown: %.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DNOTES=1 -DDOCX=1 ${PPFLAGS} $< -o $@

%.notes.ipynb.markdown: %.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DIPYNB=1 -DNOTES=1 ${PPFLAGS} $< -o $@

%.slides.ipynb.markdown: %.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DIPYNB=1 -DSLIDES=1 ${PPFLAGS} $< -o $@


%.pdf: %.svg
	/Applications/Inkscape.app/Contents/Resources/bin/inkscape $< -A=$@ --without-gui

%.png: %.svg
	/Applications/Inkscape.app/Contents/Resources/bin/inkscape $< -A=$@ --without-gui

clean:
	rm ${BASE}.slides.html.markdown \
		${BASE}.slides.html \
		${BASE}.notes.docx.markdown \
		${BASE}.notes.docx \
		${BASE}.notes.tex.markdown \
		${BASE}.notes.tex \
		${BASE}.notes.out \
		${BASE}.notes.log \
		${BASE}.notes.bbl \
		${BASE}.notes.aux \
		${BASE}.notes.html.markdown \
		${BASE}.notes.html \
		${BASE}.posts.html \
		${BASE}.ipynb \
		${BASE}.slides.ipynb.markdown \
		${BASE}.slides.ipynb
