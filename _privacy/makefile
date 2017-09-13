cloaking-functions.slides.html: cloaking-functions.slides.md
	pandoc -s -S -c talks.css -t revealjs --mathjax="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" -o cloaking-functions.slides.html  cloaking-functions.slides.md

cloaking-functions.slides.md: cloaking-functions.md
	gpp -T cloaking-functions.md -o cloaking-functions.slides.md


clean:
	rm cloaking-functions.slides.md cloaking-functions.slides.html
