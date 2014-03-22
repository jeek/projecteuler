import fileinput

for line in fileinput.input():
    (i, j) = line.split(" ")
    print i
    print j
    