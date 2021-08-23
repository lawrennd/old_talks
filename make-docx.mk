%.notes.docx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to docx --code sparse --diagrams-dir ../slides/diagrams --edit-links ${PPFLAGS} --replace-notation



${BASE}.docx: ${BASE}.notes.docx.markdown ${DOCXDEPS}
	pandoc  -s \
		${BIBFLAGS} \
		${DOCXFLAGS} \
		-o ${BASE}.docx  \
		${BASE}.notes.docx.markdown 

