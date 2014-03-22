from collections import defaultdict
maxvalue = 1000000
mdrs = defaultdict(int)

array = [2]
mdrs[2] = 2

while array[0] < maxvalue:
    array.append(array[-1])
    product = 1
    for x in array:
        product *= x
    while product >= maxvalue:
        array.pop()
        array[-1] += 1
        product = 1
        for x in array:
            product *= x
    drs = ""
    for i in array:
        drs += str(i)
    drstotal = 0
    for i in drs:
        drstotal += int(i)
    if drstotal > mdrs[product]:
        mdrs[product] = drstotal
        print product, drstotal, sum(mdrs.values()), array #, mdrs
  