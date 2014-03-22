rules = [("90342", 2),
         ("70794", 0),
         ("39458", 2),
         ("34109", 1),
         ("51545", 2),
         ("12531", 1)]
rules = [("5616185650518293", 2),
         ("3847439647293047", 1),
         ("5855462940810587", 3),
         ("9742855507068353", 3),
         ("4296849643607543", 3),
         ("3174248439465858", 1),
         ("4513559094146117", 2),
         ("7890971548908067", 3),
         ("8157356344118483", 1),
         ("2615250744386899", 2),
         ("8690095851526254", 3),
         ("6375711915077050", 1),
         ("6913859173121360", 1),
         ("6442889055042768", 2),
         ("2321386104303845", 0),
         ("2326509471271448", 2),
         ("5251583379644322", 2),
         ("1748270476758276", 3),
         ("4895722652190306", 1),
         ("3041631117224635", 3),
         ("1841236454324589", 3),
         ("2659862637316867", 2)]


numberlength = len(rules[0][0])
print numberlength
print

rulesmatrix = []
rownumber = -1

def possible(rule):
    (actualstring, stringcount) = rule
    for i in range(2 ** numberlength):
        bitcount = 0
        j = i
        while j:
            j &= j - 1
            bitcount += 1
        if bitcount == stringcount:
            result = []
            for j in range(numberlength):
                if 2 ** j & i > 0:
                    result.append((j, int(actualstring[j]), 1))
                else:
                    result.append((j, int(actualstring[j]), 0))
            yield set(result)

for i in rules:
    rownumber += 1
    rulesmatrix.append([])
    for j in possible(i):
        rulesmatrix[rownumber].append(j)
rulesmatrix = sorted(rulesmatrix, key = len)

#print rulesmatrix
for i in rulesmatrix:
    print len(i)