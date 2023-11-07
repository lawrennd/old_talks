%.notes.tex.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to tex --code sparse --diagrams-dir diagrams --edit-links ${PPFLAGS} 
	# Fix percentage width for latex.
	sed -i -e 's/width=\(.*\)\%/width=0.\1\\textwidth/g' $@
	sed -i -e 's/height=\(.*\)\%/height=0.\1\\textheight/g' $@


${BASE}.notes.pdf: ${BASE}.notes.aux ${BASE}.notes.bbl ${BASE}.notes.tex
	pdflatex -shell-escape ${BASE}.notes.tex
	cp ${BASE}.notes.pdf ${NOTESDIR}/${OUT}.notes.pdf

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
		-B ../_includes/${NOTATION} \
		-o ${BASE}.notes.tex  \
		${BASE}.notes.tex.markdown 

${BASE}.include.tex: ${BASE}.notes.tex.markdown ${TEXDEPS}
	pandoc  -s \
		--template pandoc-include-tex-template.tex \
		--number-sections \
		--natbib \
		${BIBFLAGS} \
		-B ../_includes/${NOTATION} \
		-o ${BASE}.include.tex  \
		${BASE}.notes.tex.markdown 
	cp ${BASE}.include.tex ${TEXDIR}/${BASE}.include.tex
	../copy_web_diagrams.sh ${BASE}.md texdiagrams ${TEXDIR}/diagrams	
