${BASE}.py: ${BASE}.plots.py.markdown
	cp $< $@

${BASE}_all.py: ${BASE}.all.py.markdown
	cp $< $@
