all: problem008.out

problem008.out: problem008.py
	python problem008.py > problem008.out

test: problem008.py
	python -munittest problem008

clean:
	rm -rf *~ *.pyc *.out
