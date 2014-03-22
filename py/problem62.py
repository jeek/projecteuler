from collections import defaultdict

i = 1
done = 0
answers = defaultdict(int)
minname = dict()
while done == 0:
    name = str.join("",sorted(str(i ** 3)))
    answers[name] += 1
    if not minname.has_key(name):
        minname[name] = i ** 3
    if answers[name] == 5:
        done = 1
        print minname[name]
    i += 1