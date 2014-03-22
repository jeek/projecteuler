puzzle = []
for column in range(9):
    puzzle.append([])
    for row in range(9):
        puzzle[-1].append([x for x in range(1, 10)])
print puzzle
