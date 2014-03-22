from gmpy import is_square

answers = []

i = 0
max = 0
while len(answers) != 47547:
    i += 1
    answers = [j for j in range(1, 2 * i) if is_square(i ** 2 + j ** 2)]
    if len(answers) > max:
        print i, len(answers)
        max = len(answers)
print i