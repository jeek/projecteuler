all: problem001.out problem002.out problem003.out problem004.out problem005.out problem006.out problem007.out problem008.out problem009.out problem010.out problem012.out problem020.out problem021.out

clean:
	rm -rf *.out *.pyc *~

test:
	ls *.py|sed 's/.py\$//'|xargs python -munittest

problem001.out: problem001.py
	python problem001.py > problem001.out

problem002.out: problem002.py fibonacci.py
	python problem002.py > problem002.out

problem003.out: problem003.py factors.py
	python problem003.py > problem003.out

problem004.out: problem004.py
	python problem004.py > problem004.out

problem005.out: problem005.py
	python problem005.py > problem005.out

problem006.out: problem006.py
	python problem006.py > problem006.out

problem007.out: primes.py problem007.py
	python problem007.py > problem007.out

problem008.out: problem008.py
	python problem008.py > problem008.out

problem009.out: problem009.py
	python problem009.py > problem009.out

problem010.out: problem010.py
	python problem010.py > problem010.out

problem012.out: problem012.py
	python problem012.py > problem012.out

problem020.out: factorial.py sumofdigits.py problem020.py
	python problem020.py > problem020.out

problem021.out: divisors.py problem021.py
	python problem021.py > problem021.out
