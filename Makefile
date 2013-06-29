all:

clean:
	rm -rf *~ *.pyc *.out

test:
	python -munittest fibonacci
