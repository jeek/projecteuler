def sumofdigits(argument = 0):
    answer = 0
    while argument > 0:
        answer += argument % 10
        argument = int(argument / 10)
    return answer
