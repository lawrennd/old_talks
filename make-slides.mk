${BASE}.slides.html: ${BASE}.slides.html.markdown ${BIBDEPS}
	#printf '' > ../include.tmp
	#printf '\[' >> ../include.tmp
	#cat ../_includes/${NOTATION} >> ../include.tmp
	#printf '\]' >> ../include.tmp
	#printf '' >> ../include.tmp
	#pandoc  --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=../_includes/${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.html.markdown 
	pandoc --template pandoc-revealjs-template ${PDSFLAGS} ${SFLAGS} -c ${CSS} --include-in-header=../_includes/${SLIDESHEADER} -t revealjs --bibliography=../lawrence.bib --bibliography=../other.bib --bibliography=../zbooks.bib -o ${BASE}.slides.html  ${BASE}.slides.html.markdown 
	cp ${BASE}.slides.html ${SLIDEDIR}/${OUT}.slides.html
	../copy_web_diagrams.sh ${BASE}.md
	#rm ../include.tmp

${BASE}.pptx: ${BASE}.slides.pptx.markdown 
	pandoc  -t pptx \
		-o $@ $< \
		-B ../_includes/${NOTATION} \
		${PPTXFLAGS} \
		${CITEFLAGS} \
		${SFLAGS}
