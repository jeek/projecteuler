all: problem001.out problem002.out problem003.out

clean:
	rm -rf *.out *.pyc *~

test:
	python -munittest problem001 problem002 fibonacci factors problem003

problem001.out: problem001.py
	python problem001.py > problem001.out

problem002.out: problem002.py fibonacci.py
	python problem002.py > problem002.out

problem003.out: problem003.py factors.py
	python problem003.py > problem003.out
