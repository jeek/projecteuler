all: problem004.out

clean:
	rm -rf *~ *.out *.pyc

test:
	python -munittest reverseint palindrome problem004

problem004.out: problem004.py
	python problem004.py > problem004.out


