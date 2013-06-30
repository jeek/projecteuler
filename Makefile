all: problem005.out

test:
	python -munittest gcd problem005

clean:
	rm -rf *.out *~ *.pyc

problem005.out: problem005.py
	python problem005.py > problem005.out