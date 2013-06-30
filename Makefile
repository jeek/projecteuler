all:

clean:
	rm -rf *~ *.out *.pyc

test:
	python -munittest primes
