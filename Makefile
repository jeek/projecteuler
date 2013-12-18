export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH

all: problem001 problem002 problem003 problem004 problem005 problem006 problem007 problem008 problem009 problem010 problem011

problem001: problem001.cpp
	g++ -o problem001 problem001.cpp

problem002: problem002.cpp
	g++ -o problem002 problem002.cpp

problem003: problem003.cpp
	g++ -o problem003 problem003.cpp

problem004: problem004.cpp libispalindrome.so
	g++ -o problem004 problem004.cpp -Wl,-rpath=./ -L./ -lispalindrome

libispalindrome.so: ispalindrome.o ispalindrome.o
	g++ -shared -o libispalindrome.so ispalindrome.o

problem005: problem005.cpp liblcm.so libgcd.so
	g++ -o problem005 problem005.cpp -Wl,-rpath=./ -L./ -lgcd -llcm

liblcm.so: lcm.o gcd.o
	g++ -shared -o liblcm.so lcm.o -Wl,-rpath=./ -L./ -lgcd

libgcd.so: gcd.o
	g++ -shared -o libgcd.so gcd.o

problem006: problem006.cpp
	g++ -o problem006 problem006.cpp

problem007: problem007.cpp
	g++ -o problem007 problem007.cpp

problem008: problem008.cpp
	g++ -o problem008 problem008.cpp

problem009: problem009.cpp
	g++ -o problem009 problem009.cpp

problem010: problem010.cpp
	g++ -o problem010 problem010.cpp

problem011: problem011.cpp
	g++ -o problem011 problem011.cpp

problem012: problem012.cpp
	g++ -o problem012 problem012.cpp

ispalindrome.o: ispalindrome.cpp ispalindrome.h
	g++ -c -Wall -Werror -fpic ispalindrome.cpp

gcd.o: gcd.cpp gcd.h
	g++ -c -Wall -Werror -fpic gcd.cpp

lcm.o: lcm.cpp lcm.h libgcd.so
	g++ -c -Wall -Werror -fpic lcm.cpp

problem001.out: problem001
	./problem001 > problem001.out

problem001test.out: problem001
	./problem001 10 > problem001test.out

problem002.out: problem002
	./problem002 > problem002.out

problem003.out: problem003
	./problem003 > problem003.out

problem003test.out: problem003
	./problem003 13195 > problem003test.out

problem004.out: problem004
	./problem004 > problem004.out

problem004test.out: problem004
	./problem004 2 > problem004test.out

problem005.out: problem005
	./problem005 > problem005.out

problem005test.out: problem005
	./problem005 10 > problem005test.out

problem006.out: problem006
	./problem006 > problem006.out

problem006test.out: problem006
	./problem006 10 > problem006test.out

problem007.out: problem007
	./problem007 > problem007.out

problem007test.out: problem007
	./problem007 6 > problem007test.out

problem008.out: problem008
	./problem008 > problem008.out

problem009.out: problem009
	./problem009 > problem009.out

problem010.out: problem010
	./problem010 > problem010.out

problem010test.out: problem010
	./problem010 10 > problem010test.out

problem011.out: problem011
	./problem011 > problem011.out

problem012.out: problem012
	./problem012 > problem012.out

problem012test.out: problem012
	./problem012 5 > problem012test.out

test: problem001test.out problem001.out problem002.out \
	problem003test.out problem003.out problem004test.out problem004.out \
	problem005test.out problem005.out problem006test.out problem006.out \
	problem007test.out problem007.out problem008.out problem009.out \
	problem010test.out problem010.out problem011.out problem012test.out \
	problem012.out
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
	@ echo 011: 70600674 | diff problem011.out -
	@ echo 012: 28 | diff problem012test.out -
	@ echo 012: 76576500 | diff problem012.out -
clean:
	rm -rf *~ problem??? problem*.out *.o *.so
