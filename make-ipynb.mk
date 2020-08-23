${BASE}.ipynb: ${BASE}.notes.ipynb.markdown
	pandoc  --template pandoc-jekyll-ipynb-template \
		--atx-headers \
		-B ../_includes/talk-notation.tex \
		--out ${BASE}.tmp.markdown  ${BASE}.notes.ipynb.markdown
	pandoc 	${PDSFLAGS} \
		--out $@ ${BASE}.tmp.markdown
	#notedown ${BASE}.tmp.markdown > ${BASE}.ipynb
	cp ${BASE}.ipynb ${NOTEBOOKDIR}/${OUT}.ipynb
	rm ${BASE}.tmp.markdown

${BASE}.full.ipynb: ${BASE}.full.ipynb.markdown
	pandoc  --template pandoc-jekyll-ipynb-template \
		--atx-headers \
		-B ../_includes/talk-notation.tex \
		--out ${BASE}.tmp.markdown  ${BASE}.full.ipynb.markdown
	pandoc 	${PDSFLAGS} \
		--out $@ ${BASE}.tmp.markdown
	#notedown ${BASE}.tmp.markdown > ${BASE}.ipynb
	cp ${BASE}.full.ipynb ${NOTEBOOKDIR}/${OUT}.full.ipynb
	rm ${BASE}.tmp.markdown

${BASE}.slides.ipynb: ${BASE}.slides.ipynb.markdown
	pandoc  --template pandoc-jekyll-ipynb-template \
		--atx-headers \
		-B ../_includes/talk-notation.tex \
		${CITEFLAGS} \
		--out ${BASE}.tmp.markdown  ${BASE}.slides.ipynb.markdown
	notedown ${BASE}.tmp.markdown > ${BASE}.slides.ipynb
	cp ${BASE}.slides.ipynb ${NOTEBOOKDIR}/${OUT}.slides.ipynb
	rm ${BASE}.tmp.markdown
