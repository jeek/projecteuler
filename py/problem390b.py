import gmpy

n = 10 ** 10
total = 0

c = 2
queue = []
while gmpy.sqrt((c ** 2 * 2) + c ** 2 + (c ** 2 * 2) ** 2 * c ** 2)/2 < n:
    b = (c ** 2) * 2
    if gmpy.is_square(b ** 2 + c ** 2 + b ** 2 * c ** 2) and ((gmpy.sqrt(b ** 2 + c ** 2 + b ** 2 * c ** 2) % 2) == 0):
        queue.append(b)
#        if c < 20:
        queue.append(c)
#        else:
#        total += (gmpy.sqrt(b ** 2 + c ** 2 + b ** 2 * c ** 2)) / 2
        d = 8 * c ** 4 + 4 * c ** 2
        queue.append(d)
#        total += (gmpy.sqrt(d ** 2 + c ** 2 + d ** 2 * c ** 2)) / 2
    print total, c
    c += 2

b = 2
done = dict()
while (len(queue) > 0):
    queue = sorted(queue)
    c = queue.pop()
    if done.has_key(c):
        pass
    else:
        done[c] = 1
        b = c + 2
        dd = b ** 2 + c ** 2 + b ** 2 * c ** 2
        while ((gmpy.sqrt(dd))/2 < n):
            if (gmpy.is_square(dd) and (gmpy.sqrt(dd)) % 2 == 0):
                total += (gmpy.sqrt(dd)) / 2
                print total,b,c
                queue.append(c)
                queue.append(b)
            b += 2
            dd = b ** 2 + c ** 2 + b ** 2 * c ** 2
    print total,"Queue Length:",len(queue)