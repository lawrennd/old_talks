%.paper.tex.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to tex --code none ${PPFLAGS} 
	# Fix percentage width for latex.
	sed -i -e 's/width=\(.*\)\%/width=0.\1\\textwidth/g' $@
	sed -i -e 's/height=\(.*\)\%/height=0.\1\\textheight/g' $@

${BASE}.paper.pdf: ${BASE}.paper.aux ${BASE}.paper.bbl ${BASE}.paper.tex
	pdflatex -shell-escape ${BASE}.paper.tex
	cp ${BASE}.paper.pdf ${NOTEDIR}/${OUT}.paper.pdf

${BASE}.paper.bbl: ${BASE}.paper.aux ${BIBDEPS}
	bibtex ${BASE}.notes

${BASE}.paper.aux: ${BASE}.paper.tex
	pdflatex -shell-escape ${BASE}.paper.tex


${BASE}.paper.tex: ${BASE}.paper.tex.markdown 
	pandoc  -s \
		--template pandoc-notes-tex-template.tex \
		--number-sections \
		--natbib \
		${BIBFLAGS} \
		-B ../_includes/${NOTATION} \
		-o ${BASE}.paper.tex  \
		${BASE}.paper.tex.markdown 
