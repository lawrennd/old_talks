%.notes.docx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to docx --code sparse --snippets-path ${SNIPPETSDIR} --diagrams-dir ${DIAGRAMSDIR} --edit-links ${PPFLAGS} --replace-notation


${BASE}.docx: ${BASE}.notes.docx.markdown ${DOCXDEPS}
	pandoc  -s \
		--resource-path=.:.. \
		${CITEFLAGS} \
		${DOCXFLAGS} \
		-B ../_includes/${NOTATION} \
		-o ${BASE}.docx  \
		${BASE}.notes.docx.markdown 

