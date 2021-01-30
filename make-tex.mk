${BASE}.notes.pdf: ${BASE}.notes.aux ${BASE}.notes.bbl ${BASE}.notes.tex
	pdflatex -shell-escape ${BASE}.notes.tex
	cp ${BASE}.notes.pdf ${NOTEDIR}/${OUT}.notes.pdf

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
