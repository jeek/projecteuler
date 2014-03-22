answers = range(1, 10)[::-1]
import random

linenumber = 0
while len(answers):
#    current = answers.pop(random.randint(0, len(answers) - 1))
    current = answers.pop()
    if current < 10 ** 40:
        temp = str(current)
        if "1" in temp and "2" in temp and "3" in temp and "4" in temp and "5" in temp and "6" in temp and "7" in temp and "8" in temp and "9" in temp and "0" in temp:
            linenumber += 1
            print linenumber, len(answers), current
        if (current % 10) < 9:
            answers.append(current * 10 + current % 10 + 1)
   #     else:
  #          answers.append(current * 10)
        if (current % 10) > 0:
            answers.append(current * 10 + current % 10 - 1)
#        else:
 #           answers.append(current * 10 + 9)
