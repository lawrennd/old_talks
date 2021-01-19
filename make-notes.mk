
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

