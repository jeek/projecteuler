all: problem003.out

problem003.out: problem003.py factors.py
	python problem003.py > problem003.out

test:
	python -munittest primes factors problem003

clean:
	rm -rf *.pyc *~ *.out
