%.notes.docx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to docx --code sparse --diagrams-dir ../slides/diagrams --edit-links ${PPFLAGS} 



${BASE}.docx: ${BASE}.notes.docx.markdown 
	pandoc  -s \
		${BIBFLAGS} \
		${DOCXFLAGS} \
		-B ../_includes/${NOTATION} \
		-o ${BASE}.notes.docx  \
		${BASE}.notes.docx.markdown 

