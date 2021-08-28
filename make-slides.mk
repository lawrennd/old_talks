%.slides.pptx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --to pptx --format slides --code none ${PPFLAGS} --diagrams-dir ../slides/diagrams  --replace-notation

%.slides.html.markdown: %.md ${DEPS}
	${PP} $< -o $@ --to html --format slides --code none ${PPFLAGS} --replace-notation


${BASE}.slides.html: ${BASE}.slides.html.markdown ${BIBDEPS}
	pandoc --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} --include-in-header=../_includes/${SLIDESHEADER} -t revealjs ${BIBFLAGS} -o ${BASE}.slides.html  ${BASE}.slides.html.markdown 
	cp ${BASE}.slides.html ${SLIDESDIR}/${OUT}.slides.html

${BASE}.pptx: ${BASE}.slides.pptx.markdown 
	pandoc  -t pptx \
		-o $@ $< \
		${PPTXFLAGS} \
		${CITEFLAGS} \
		${SFLAGS}
