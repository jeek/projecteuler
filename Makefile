all: problem007.out

clean:
	rm -rf *~ *.out *.pyc

test: primes.py problem007.py
	python -munittest primes problem007

problem007.out: primes.py problem007.py
	python problem007.py > problem007.out
