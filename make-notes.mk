%.notes.html.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to html --code sparse --diagrams-dir ${DIAGRAMSDIR} --replace-notation --edit-links --exercises ${PPFLAGS} 

%.notes.docx.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to docx --code sparse --replace-notation --edit-links ${PPFLAGS}
	echo ${BASE}


${BASE}.notes.html: ${BASE}.notes.html.markdown ${BIBDEPS}
	pandoc  ${PDSFLAGS} \
		--mathjax \
		-o ${BASE}.notes.html  \
		${BASE}.notes.html.markdown 

