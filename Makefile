all: problem006.out

clean:
	rm -rf *~ *.pyc *.out

problem006.out: problem006.py
	python problem006.py > problem006.out

test: problem006.py
	python -munittest problem006
