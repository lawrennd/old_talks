# Check header for which formats to create in notes and slides.
# CReate PDF Of reveal slides with something like decktape https://github.com/astefanutti/decktape

OUT=$(PREFIX)-$(BASE)

all: $(ALL)

##${BASE}.notes.tex ${BASE}.notes.pdf 

include ../make-slides.mk 
include ../make-notes.mk
include ../make-post.mk
include ../make-ipynb.mk
include ../make-markdown.mk
include ../make-figures.mk


clean:
	rm *.markdown
	rm *.markdown-e
	rm ${ALL}
