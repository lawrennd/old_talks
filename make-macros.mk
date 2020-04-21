DOWNLOAD_URL=https://raw.githubusercontent.com/lawrennd/macros/master
MACROS=macros
DEPFILE=makedependency_talk.py
DEPS=$(shell ./$(DEPFILE) $(MACROS))

all: talk-macros.gpp

talk-macros.gpp: dummy

%.gpp:
	# Download the file
	wget -O $@ $(DOWNLOAD_URL)/gpp/$@
	touch dummy
	DEPS=$(shell ./$(DEPFILE) $@)
	echo $(DEPS)
	# Call recursively
	$(MAKE) $(DEPS)

dummy:
	touch dummy

clean:
	rm *.gpp
	rm dummy
