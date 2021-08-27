%.notes.docx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to docx --code sparse --diagrams-dir ../slides/diagrams --edit-links ${PPFLAGS} --replace-notation



${BASE}.docx: ${BASE}.notes.docx.markdown ${DOCXDEPS}
	pandoc  -s \
		${CITEFLAGS} \
		${DOCXFLAGS} \
		-B ../_includes/${NOTATION} \
		-o ${BASE}.docx  \
		${BASE}.notes.docx.markdown 

