${BASE}.slides.html: ${BASE}.slides.html.markdown ${BIBDEPS}
	pandoc --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=../_includes/${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.html.markdown 
	cp ${BASE}.slides.html ${SLIDEDIR}/${OUT}.slides.html
	../copy_web_diagrams.sh ${BASE}.md

${BASE}.pptx: ${BASE}.slides.pptx.markdown 
	pandoc  -t pptx \
		-o $@ $< \
		-B ../_includes/${NOTATION} \
		${PPTXFLAGS} \
		${CITEFLAGS} \
		${SFLAGS}
