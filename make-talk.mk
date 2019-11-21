# Check header for which formats to create in notes and slides.
# CReate PDF Of reveal slides with something like decktape https://github.com/astefanutti/decktape

OUT=$(DATE)-$(BASE)
DEPS=$(shell ../dependencies.py inputs $(BASE).md)
DIAGDEPS=$(shell ../dependencies.py diagrams $(BASE).md)
BIBDEPS=$(shell ../dependencies.py bibinputs $(BASE).md)
POSTFLAGS=$(shell ../flags.py post $(BASE))
PPTXFLAGS=$(shell ../flags.py pptx $(BASE))
DOCXFLAGS=$(shell ../flags.py docx $(BASE))
ALL=$(shell ../dependencies.py all $(BASE).md)

all: $(ALL)

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

${BASE}.pptx: ${BASE}.slides.pptx.markdown 
	pandoc  -t pptx \
		-o $@ $< \
		-B ../_includes/talk-notation.tex \
		${PPTXFLAGS} \
		${CITEFLAGS} \
		${SFLAGS} 

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

${BASE}.docx: ${BASE}.notes.docx.markdown ${BIBDEPS} ${DIAGDEPS}
	pandoc  ${CITEFLAGS} \
		--to docx \
		-B ../_includes/talk-notation.tex \
		${DOCXFLAGS} \
		--out ${BASE}.docx  \
		${BASE}.notes.docx.markdown 

${BASE}.notes.html: ${BASE}.notes.html.markdown ${BIBDEPS}
	pandoc  ${PDSFLAGS} \
		-o ${BASE}.notes.html  \
		${BASE}.notes.html.markdown 

${BASE}.posts.html: ${BASE}.notes.html.markdown
	pandoc --template pandoc-jekyll-talk-template ${PDFLAGS} \
	       --atx-headers \
	       ${POSTFLAGS} \
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


${BASE}.slides.pptx.markdown: ${BASE}.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DPPTX=1 -DSLIDES=1 ${PPFLAGS} --include ../_includes/talk-notation.tex $< -o $@  

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
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DNOTES=1 -DDOCX=1 ${PPFLAGS} --include ../_includes/talk-notation.tex $< -o $@

%.notes.ipynb.markdown: %.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DIPYNB=1 -DNOTES=1 ${PPFLAGS} $< -o $@

%.slides.ipynb.markdown: %.md ${DEPS}
	${PP} -U "\\" "" "{" "}{" "}" "{" "}" "#" "" -DIPYNB=1 -DSLIDES=1 ${PPFLAGS} $< -o $@


%.pdf: %.svg
	${INKSCAPE} $< --export-pdf=$@ --without-gui

%.png: %.svg
	${INKSCAPE} $< --export-png=$@ --without-gui

%.emf: %.svg
	${INKSCAPE} $< --export-emf=$@ --without-gui

clean:
	rm ${ALL} \
	${BASE}.slides.html.markdown \
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
