import gmpy

answers = []
i = 0

while (len(answers) < 2000):
    i += 1
    if gmpy.is_prime(6 * i + 1) and gmpy.is_prime(6 * i - 1) and gmpy.is_prime(12 * i + 5):
        answers.append(3*i*(i-1)+2)
        print 3*i*(i-1)+2