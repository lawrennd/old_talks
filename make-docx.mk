%.notes.docx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to docx --code sparse --diagrams-dir diagrams --edit-links ${PPFLAGS} 



${BASE}.notes.docx: ${BASE}.notes.docx.markdown 
	pandoc  -s \
		${BIBFLAGS} \
		-B ../_includes/${NOTATION} \
		-o ${BASE}.notes.docx  \
		${BASE}.notes.docx.markdown 

