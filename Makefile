export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH

all: projecteuler

projecteuler: projecteuler.cpp libproblem001.so libproblem002.so libproblem003.so libproblem004.so liblcm.so libgcd.so libproblem005.so libabs.so libproblem006.so libproblem007.so libproblem008.so libproblem009.so libproblem010.so
	g++ -Wl,-rpath=./ -L./ -o projecteuler projecteuler.cpp -lproblem001 -lproblem002 -lproblem003 -lproblem004 -lproblem005 -lgcd -llcm -lproblem006 -labs -lproblem007 -lproblem008 -lproblem009 -lproblem010

libproblem001.so: problem001.o
	g++ -shared -o libproblem001.so problem001.o

libproblem002.so: problem002.o
	g++ -shared -o libproblem002.so problem002.o

libproblem003.so: problem003.o
	g++ -shared -o libproblem003.so problem003.o

libproblem004.so: problem004.o ispalindrome.o
	g++ -shared -o libproblem004.so problem004.o -Wl,-rpath=./ -L./ -lispalindrome

libispalindrome.so: ispalindrome.o ispalindrome.o
	g++ -shared -o libispalindrome.so ispalindrome.o

libproblem005.so: problem005.o lcm.o gcd.o
	g++ -shared -o libproblem005.so problem005.o -Wl,-rpath=./ -L./ -lgcd -llcm

liblcm.so: lcm.o gcd.o
	g++ -shared -o liblcm.so lcm.o -Wl,-rpath=./ -L./ -lgcd

libgcd.so: gcd.o
	g++ -shared -o libgcd.so gcd.o

libabs.so: abs.o
	g++ -shared -o libabs.so abs.o

libproblem006.so: problem006.o abs.o
	g++ -shared -o libproblem006.so problem006.o -Wl,-rpath=./ -L./ -labs

libproblem007.so: problem007.o
	g++ -shared -o libproblem007.so problem007.o

libproblem008.so: problem008.o
	g++ -shared -o libproblem008.so problem008.o

libproblem009.so: problem009.o
	g++ -shared -o libproblem009.so problem009.o

libproblem010.so: problem010.o
	g++ -shared -o libproblem010.so problem010.o

problem001.o: problem001.cpp problem001.h
	g++ -c -Wall -Werror -fpic problem001.cpp

problem002.o: problem002.cpp problem002.h
	g++ -c -Wall -Werror -fpic problem002.cpp

problem003.o: problem003.cpp problem003.h
	g++ -c -Wall -Werror -fpic problem003.cpp

problem004.o: problem004.cpp problem004.h libispalindrome.so
	g++ -c -Wall -Werror -fpic problem004.cpp

ispalindrome.o: ispalindrome.cpp ispalindrome.h
	g++ -c -Wall -Werror -fpic ispalindrome.cpp

problem005.o: problem005.cpp problem005.h liblcm.so
	g++ -c -Wall -Werror -fpic problem005.cpp

problem006.o: problem006.cpp problem006.h libabs.so
	g++ -c -Wall -Werror -fpic problem006.cpp

gcd.o: gcd.cpp gcd.h
	g++ -c -Wall -Werror -fpic gcd.cpp

lcm.o: lcm.cpp lcm.h libgcd.so
	g++ -c -Wall -Werror -fpic lcm.cpp

abs.o: abs.cpp abs.h
	g++ -c -Wall -Werror -fpic abs.cpp

problem007.o: problem007.cpp problem007.h
	g++ -c -Wall -Werror -fpic problem007.cpp

problem008.o: problem008.cpp problem008.h
	g++ -c -Wall -Werror -fpic problem008.cpp

problem009.o: problem009.cpp problem009.h
	g++ -c -Wall -Werror -fpic problem009.cpp

problem010.o: problem010.cpp problem010.h
	g++ -c -Wall -Werror -fpic problem010.cpp

problem001.out: projecteuler
	./projecteuler 1 > problem001.out

problem001test.out: projecteuler
	./projecteuler 1 10 > problem001test.out

problem002.out: projecteuler
	./projecteuler 2 > problem002.out

problem003.out: projecteuler
	./projecteuler 3 > problem003.out

problem003test.out: projecteuler
	./projecteuler 3 13195 > problem003test.out

problem004.out: projecteuler
	./projecteuler 4 > problem004.out

problem004test.out: projecteuler
	./projecteuler 4 2 > problem004test.out

problem005.out: projecteuler
	./projecteuler 5 > problem005.out

problem005test.out: projecteuler
	./projecteuler 5 10 > problem005test.out

problem006.out: projecteuler
	./projecteuler 6 > problem006.out

problem006test.out: projecteuler
	./projecteuler 6 10 > problem006test.out

problem007.out: projecteuler
	./projecteuler 7 > problem007.out

problem007test.out: projecteuler
	./projecteuler 7 6 > problem007test.out

problem008.out: projecteuler
	./projecteuler 8 > problem008.out

problem009.out: projecteuler
	./projecteuler 9 > problem009.out

problem010.out: projecteuler
	./projecteuler 10 > problem010.out

problem010test.out: projecteuler
	./projecteuler 10 10 > problem010test.out

test: projecteuler problem001test.out problem001.out problem002.out \
	problem003test.out problem003.out problem004test.out problem004.out \
	problem005test.out problem005.out problem006test.out problem006.out \
	problem007test.out problem007.out problem008.out problem009.out \
	problem010test.out problem010.out
	@ echo 001: 23 | diff problem001test.out -
	@ echo 001: 233168 | diff problem001.out -
	@ echo 002: 4613732 | diff problem002.out -
	@ echo 003: 29 | diff problem003test.out -
	@ echo 003: 6857 | diff problem003.out -
	@ echo 004: 9009 | diff problem004test.out -
	@ echo 004: 906609 | diff problem004.out -
	@ echo 005: 2520 | diff problem005test.out -
	@ echo 005: 232792560 | diff problem005.out -
	@ echo 006: 2640 | diff problem006test.out -
	@ echo 006: 25164150 | diff problem006.out -
	@ echo 007: 13 | diff problem007test.out -
	@ echo 007: 104743 | diff problem007.out -
	@ echo 008: 40824 | diff problem008.out -
	@ echo 009: 31875000 | diff problem009.out -
	@ echo 010: 17 | diff problem010test.out -
	@ echo 010: 142913828922 | diff problem010.out -

clean:
	rm -rf *~ projecteuler problem*.out *.o *.so
