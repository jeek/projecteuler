for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            for d in [0, 1]:
                for e in [0, 1]:
                    for f in [0, 1]:
                        if a & b == 0:
                            if b & c == 0:
                                if c & d == 0:
                                    if d & e == 0:
                                        if e & f == 0:
                                            if f & (a ^ (b & c)):
                                                print "HA!"