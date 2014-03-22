pb = 32

def dice():
    for i in range(8,19,2):
        yield i
def points(i):
    return [0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,8,10,13,16][i]
for a in dice():
    for b in dice():
        for c in dice():
            for d in [8]:
                for e in dice():
                    for f in dice():
                        if points(a) + points(b) + points(c) + points(d) + points(e) + points(f) == pb:
                            print "STR",a+4, "DEX",b,"CON", c, "INT", d-2, "WIS", e-2, "CHA", f-2