bin_PROGRAMS = problem001 problem002 problem003 problem004 problem005 \
    problem006 problem007 problem008 problem009 problem010 problem011 \
    problem012 problem013
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

problem009_SOURCES = problem009.cpp
problem009_LDADD = $(INTI_LIBS)

problem010_SOURCES = problem010.cpp
problem010_LDADD = $(INTI_LIBS)

problem011_SOURCES = problem011.cpp
problem011_LDADD = $(INTI_LIBS)

problem012_SOURCES = problem012.cpp
problem012_LDADD = $(INTI_LIBS)

problem013_SOURCES = problem013.cpp
problem013_LDADD = $(INTI_LIBS) -lgmpxx

TESTS = tests/problem001test.t tests/problem001.t \
        tests/problem002.t \
        tests/problem003test.t tests/problem003.t \
        tests/problem004test.t tests/problem004.t \
        tests/problem005test.t tests/problem005.t \
        tests/problem006test.t tests/problem006.t \
        tests/problem007test.t tests/problem007.t \
        tests/problem008.t \
        tests/problem009.t \
        tests/problem010test.t tests/problem010.t \
        tests/problem011.t \
        tests/problem012test.t tests/problem012.t \
        tests/problem013.t


