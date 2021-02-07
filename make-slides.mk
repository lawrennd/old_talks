%.slides.pptx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --to pptx --format slides --code none ${PPFLAGS} -B ../_includes/${NOTATION}

%.slides.html.markdown: %.md ${DEPS}
	${PP} $< -o $@ --to html --format slides --code none ${PPFLAGS} -B ../_includes/${NOTATION}


${BASE}.slides.html: ${BASE}.slides.html.markdown ${BIBDEPS}
	pandoc --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=../_includes/${SLIDESHEADER} -t revealjs ${BIBFLAGS} -o ${BASE}.slides.html  ${BASE}.slides.html.markdown 
	cp ${BASE}.slides.html ${SLIDEDIR}/${OUT}.slides.html
	../copy_web_diagrams.sh ${BASE}.md

${BASE}.pptx: ${BASE}.slides.pptx.markdown 
	pandoc  -t pptx \
		-o $@ $< \
		-B ../_includes/${NOTATION} \
		${PPTXFLAGS} \
		${CITEFLAGS} \
		${SFLAGS}
