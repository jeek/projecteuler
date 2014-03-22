import gmpy

def f(x):
    answer = 0
    while x > 0:
        answer += (x % 10) ** 2
        x /= 10
    return answer

x = 1
answer = 0
while x < 10 ** 20:
    if gmpy.is_square(f(x)):
        answer += f(x)
        print x, answer
    x += 1
