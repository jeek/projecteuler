bin_PROGRAMS = problem001 problem002 problem003 problem004 problem005 \
    problem006 problem007 problem008
lib_LTLIBRARIES = libispalindrome.la liblcm.la libgcd.la
libispalindrome_la_SOURCES = ispalindrome.cpp
liblcm_la_SOURCES = lcm.cpp
liblcm_la_LIBADD = libgcd.la
libgcd_la_SOURCES = gcd.cpp

LIBTOOL = `which libtool`
CLEANFILES = *.out *~

ACLOCAL_AMFLAGS = -I m4
AM_CXXFLAGS = $(INTI_CFLAGS)

problem001_SOURCES = problem001.cpp
problem001_LDADD = $(INTI_LIBS)

problem002_SOURCES = problem002.cpp
problem002_LDADD = $(INTI_LIBS)

problem003_SOURCES = problem003.cpp
problem003_LDADD = $(INTI_LIBS)

problem004_SOURCES = problem004.cpp
problem004_LDADD = $(INTI_LIBS) libispalindrome.la

problem005_SOURCES = problem005.cpp
problem005_LDADD = $(INTI_LIBS) liblcm.la

problem006_SOURCES = problem006.cpp
problem006_LDADD = $(INTI_LIBS)

problem007_SOURCES = problem007.cpp
problem007_LDADD = $(INTI_LIBS)

problem008_SOURCES = problem008.cpp
problem008_LDADD = $(INTI_LIBS)

TESTS = tests/problem001test.t tests/problem001.t \
        tests/problem002.t \
        tests/problem003test.t tests/problem003.t \
        tests/problem004test.t tests/problem004.t \
        tests/problem005test.t tests/problem005.t \
        tests/problem006test.t tests/problem006.t \
        tests/problem007test.t tests/problem007.t \
        tests/problem008.t
