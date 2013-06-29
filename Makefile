all: problem001.out

clean:
	rm -rf *.out *.pyc *~

test:
	python -munittest problem001

problem001.out: problem001.py
	python problem001.py > problem001.out
