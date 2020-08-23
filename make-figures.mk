%.svg: %.svgi
	${PP} $< -o $@ --format slides --to svg ${PPFLAGS} --include-before-body ../svgi-includes.gpp  --no-header

%.pdf: %.svg
	${INKSCAPE} ${PWD}/$< --export-pdf=${PWD}/$@ --without-gui

%.png: %.svg
	${INKSCAPE} ${PWD}/$< --export-png=${PWD}/$@ --without-gui

%.emf: %.svg
	${INKSCAPE} ${PWD}/$< --export-emf=${PWD}/$@ --without-gui
