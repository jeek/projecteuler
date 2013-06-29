all: problem002.out

problem002.out: problem002.py fibonacci.py
	python problem002.py > problem002.out

clean:
	rm -rf *.out *~ *.pyc

test:
	python -munittest fibonacci problem002
