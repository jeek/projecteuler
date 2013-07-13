all: problem009.out

problem009.out: problem009.py
	python problem009.py > problem009.out

clean:
	rm -rf *~ *.pyc *.out

test: problem009.py
	python -munittest problem009
