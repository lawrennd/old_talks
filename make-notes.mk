%.notes.html.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to html --code sparse --replace-notation --edit-links --exercises ${PPFLAGS} 

%.notes.docx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to docx --code sparse --replace-notation --edit-links ${PPFLAGS} 

${BASE}.docx: ${BASE}.notes.docx.markdown ${BIBDEPS} ${DIAGDEPS}
	pandoc  ${CITEFLAGS} \
		--to docx \
		-B ../_includes/${NOTATION} \
		${DOCXFLAGS} \
		--out ${BASE}.docx  \
		${BASE}.notes.docx.markdown 

${BASE}.notes.html: ${BASE}.notes.html.markdown ${BIBDEPS}
	pandoc  ${PDSFLAGS} \
		--mathjax \
		-o ${BASE}.notes.html  \
		${BASE}.notes.html.markdown 

