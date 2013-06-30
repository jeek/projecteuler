all:

test:
	python -munittest primes factors

clean:
	rm -rf *.pyc *~ *.out
