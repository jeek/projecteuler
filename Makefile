all: cpp/Makefile
	cd py;make
	cd cpp;make

cpp/Makefile:
	cd cpp;sh INSTALL

clean:	cpp/Makefile
	cd py;make clean
	cd cpp;make clean
	cd cpp;make maintainer-clean
	cd cpp;rm -rf *.cache configure Makefile.in missing *.m4 m4 config.guess config.sub depcomp install-sh ltmain.sh config.h.in configure.scan *.log

check:	cpp/Makefile
	cd cpp;make check
	cd py;make test

test:	check

distclean:	cpp/Makefile
	cd cpp;make distclean
