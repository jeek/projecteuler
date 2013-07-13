all: problem010.out

clean:
	rm -rf *~ *.out *.pyc

test: problem010.py
	python -munittest primes problem010

problem010.out: problem010.py
	python problem010.py > problem010.out
