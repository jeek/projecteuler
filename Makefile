all: problem001.out problem002.out problem003.out problem004.out problem005.out problem006.out

clean:
	rm -rf *.out *.pyc *~

test:
	python -munittest problem001 problem002 fibonacci factors problem003 \
	    reverseint palindrome problem004 gcd problem005 primes problem006

problem001.out: problem001.py
	python problem001.py > problem001.out

problem002.out: problem002.py fibonacci.py
	python problem002.py > problem002.out

problem003.out: problem003.py factors.py
	python problem003.py > problem003.out

problem004.out: problem004.py
	python problem004.py > problem004.out

problem005.out: problem005.py
	python problem005.py > problem005.out

problem006.out: problem006.py
	python problem006.py > problem006.out

