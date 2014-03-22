import sys
sys.setrecursionlimit(10000)
length = 40

def start(i, length):
    lastdigit = i % 10
    j = str(i)
#    if len(j) == length and j.find("0") > -1 and j.find("1") > -1 and j.find("2") > -1 and j.find("3") > -1 and j.find("4") > -1 and j.find("5") > -1 and j.find("6") > -1 and j.find("7") > -1 and j.find("8") > -1 and j.find("9") > -1:
    if len(j) == length:
        print j
        return
    if lastdigit != 9:
        start(i * 10 + lastdigit + 1, length)
    if lastdigit != 0:
        start(i * 10 + lastdigit - 1, length)

for i in range(1,10):
    start(i, length)