def rad(x):
    i = 2
    answer = 1
    while x > 1:
        if x % i == 0:
            answer *= i
            while x % i == 0:
                x /= i
        i += 1
    return answer

print sorted(range(1, 100001), key=rad)[9999]