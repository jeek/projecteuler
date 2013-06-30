all:

test:
	python -munittest factors

clean:
	rm -rf *.pyc *~ *.out
