%.svg: %.svgi
	${PP} $< -o $@ --format slides --to svg ${PPFLAGS} --include-before-body ../svgi-includes.gpp  --no-header

%.pdf: %.svg
	${INKSCAPE} $< --export-filename=$@ 

%.png: %.svg
	${INKSCAPE} $< --export-filename=$@ 

%.emf: %.svg
	${INKSCAPE} $< --export-filename=$@ 
