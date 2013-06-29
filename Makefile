all: problem001.out problem002.out

clean:
	rm -rf *.out *.pyc *~

test:
	python -munittest problem001 problem002 fibonacci

problem001.out: problem001.py
	python problem001.py > problem001.out

problem002.out: problem002.py fibonacci.py
	python problem002.py > problem002.out
