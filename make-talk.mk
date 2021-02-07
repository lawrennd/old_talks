# Check header for which formats to create in notes and slides.
# Create PDF of reveal slides with something like decktape https://github.com/astefanutti/decktape

OUT=$(PREFIX)$(BASE)

all: $(ALL)

##${BASE}.notes.tex ${BASE}.notes.pdf 


include ../make-slides.mk 
include ../make-notes.mk
include ../make-tex.mk
include ../make-paper.mk
include ../make-post.mk
include ../make-ipynb.mk
include ../make-figures.mk
include ../make-python.mk


clean:
	rm *.markdown
	rm *.markdown-e
	rm ${ALL}
