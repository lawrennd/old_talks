%.svg: %.svgi
	${PP} $< -o $@ --format slides --to svg ${PPFLAGS} --include-before-body ../svgi-includes.gpp  --no-header

%.pdf: %.svg
	${INKSCAPE} $< --export-pdf=$@ --without-gui

%.png: %.svg
	${INKSCAPE} $< --export-png=$@ --without-gui

%.emf: %.svg
	${INKSCAPE} $< --export-emf=$@ --without-gui
