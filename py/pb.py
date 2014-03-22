from collections import defaultdict

pointvalue = { 8: 0, 9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 8, 16: 10, 17: 13, 18: 16 }

def dice():
    result = defaultdict(int)
    for a in range(6, 0, -1):
        for b in range(6, 0, -1):
            for c in range(6, 0, -1):
                for d in range(6, 0, -1):
                    array = sorted([a, b, c, d])
                    array.pop(0)
                    result[sum(array)] += 1
    return result

dice = dice()
                   
count = 0
total = 0
for x in dice:
    count += 1
    total += x
    print x, dice[x]
    
array = [0, 0, 0, 0, 0, 0]
score = [0, 0, 0, 0, 0, 0]
modifiertotal = 0
count = 0

for array[0] in dice:
    for array[1] in dice:
        for array[2] in dice:
            for array[3] in dice:
                for array[4] in dice:
                    for array[5] in dice:
                        mult = 1
                        for x in array:
                            mult *= dice[x]
                        if 0 <= sum([int(x/2 - 5) for x in array]):
                            modifiertotal += sum([int(x/2 - 5) for x in array]) * mult
                            count += mult
    print (modifiertotal * 1.0)/count

                        