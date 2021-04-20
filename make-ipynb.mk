%.notes.ipynb.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --write-diagrams-dir . --to ipynb --code ipynb --replace-notation --edit-links --exercises ${PPFLAGS} 

%.full.ipynb.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format notes --to ipynb --code full --edit-links --replace-notation ${PPFLAGS} 

%.slides.ipynb.markdown: %.md ${DEPS}
	${PP} $< -o $@ --format slides --to ipynb ${PPFLAGS} 


${BASE}.ipynb: ${BASE}.notes.ipynb.markdown
	pandoc  --template pandoc-jekyll-ipynb-template \
		--markdown-headings=atx \
		--out ${BASE}.tmp.markdown  ${BASE}.notes.ipynb.markdown
	pandoc 	${PDSFLAGS} \
		--out $@ ${BASE}.tmp.markdown
	#notedown ${BASE}.tmp.markdown > ${BASE}.ipynb
	cp ${BASE}.ipynb ${NOTEBOOKDIR}/${OUT}.ipynb
	rm ${BASE}.tmp.markdown

${BASE}.full.ipynb: ${BASE}.full.ipynb.markdown
	pandoc  --template pandoc-jekyll-ipynb-template \
		--markdown-headings=atx \
		--out ${BASE}.tmp.markdown  ${BASE}.full.ipynb.markdown
	pandoc 	${PDSFLAGS} \
		--out $@ ${BASE}.tmp.markdown
	#notedown ${BASE}.tmp.markdown > ${BASE}.ipynb
	cp ${BASE}.full.ipynb ${NOTEBOOKDIR}/${OUT}.full.ipynb
	rm ${BASE}.tmp.markdown

${BASE}.slides.ipynb: ${BASE}.slides.ipynb.markdown
	pandoc  --template pandoc-jekyll-ipynb-template \
		--markdown-headings=atx \
		${CITEFLAGS} \
		--out ${BASE}.tmp.markdown  ${BASE}.slides.ipynb.markdown
	notedown ${BASE}.tmp.markdown > ${BASE}.slides.ipynb
	cp ${BASE}.slides.ipynb ${NOTEBOOKDIR}/${OUT}.slides.ipynb
	rm ${BASE}.tmp.markdown
