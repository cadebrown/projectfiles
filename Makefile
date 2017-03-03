
targets=$(wildcard */)

default: $(targets)

%/: FORCE
	cd $@ && $(MAKE)

FORCE:
