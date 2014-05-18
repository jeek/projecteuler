def factorial(argument = 0):
    if argument == 0:
        return 1
    bignum answer = 1
    while argument > 0:
        answer *= argument
        argument -= 1
    return answer
