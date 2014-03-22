def dice(diceleft, sides, totalleft):
    if diceleft == 0 and totalleft == 0:
        return 1
    if diceleft == 0 or totalleft < 0:
        return 1
    answer = 0
    for i in range(1, min(sides + 1, totalleft)):
        answer += dice(diceleft - 1, sides, totalleft - i)
    return answer

print dice(5, 6, 15)