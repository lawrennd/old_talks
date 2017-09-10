gpss.slides.html: gpss.slides.md
	pandoc -s -S --slide-level 3 -c tech-talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o gpss.slides.html  gpss.slides.md --filter pandoc-citeproc

gpss.slides.md: gpss.md
	gpp -T gpss.md -o gpss.slides.md


clean:
	rm gpss.slides.md gpss.slides.html
