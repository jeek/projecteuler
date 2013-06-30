all:

test:
	python -munittest gcd
	
clean:
	rm -rf *.out *~ *.pyc
		
