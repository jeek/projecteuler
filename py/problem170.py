import itertools

maxanswer = 0

for x in itertools.permutations("0123456789", 10):
    for y in range(1, 10):
        for z in range(y + 1, 10):
            a = x[:y]
            b = x[y:z]
            c = x[z:]
            aa = 0
            bb = 0
            cc = 0
            for aaa in a:
                aa *= 10
                aa += int(aaa)
            for bbb in b:
                bb *= 10
                bb += int(bbb)
            for ccc in c:
                cc *= 10
                cc += int(ccc)
            if aa > 0 and bb > 0 and cc > 0 and aa % cc == 0 and bb % cc == 0 and (str(aa).count("0") == 1 or str(bb).count("0") == 1 or str(cc).count("0") == 1):
                temp = str(cc * bb) + str(cc * aa)
                if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                    if int(temp) >= maxanswer:
                        maxanswer = int(temp)
                        print aa, bb, cc, maxanswer
                temp = str(cc * aa) + str(cc * bb)
                if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                    if int(temp) >= maxanswer:
                        maxanswer = int(temp)
                        print aa, bb, cc, maxanswer
            for zz in range(y + 1, 10):
                a = x[:y]
                b = x[y:z]
                c = x[z:zz]
                d = x[zz:]
                aa = 0
                bb = 0
                cc = 0
                dd = 0
                for aaa in a:
                    aa *= 10
                    aa += int(aaa)
                for bbb in b:
                    bb *= 10
                    bb += int(bbb)
                for ccc in c:
                    cc *= 10
                    cc += int(ccc)
                for ddd in d:
                    dd *= 10
                    dd += int(ddd)
                if aa > 0 and bb > 0 and cc > 0 and dd > 0 and aa % dd == 0 and bb % dd == 0 and cc % dd == 0 and (str(aa).count("0") == 1 or str(bb).count("0") == 1 or str(cc).count("0") == 1 or str(dd).count("0") == 1):
                    temp = str(dd * aa) + str(dd * bb) + str(dd * cc)
                    if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                        if int(temp) >= maxanswer:
                            maxanswer = int(temp)
                            print aa, bb, cc, dd, maxanswer
                    temp = str(dd * aa) + str(dd * cc) + str(dd * bb)
                    if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                        if int(temp) >= maxanswer:
                            maxanswer = int(temp)
                            print aa, bb, cc, dd, maxanswer
                    temp = str(dd * bb) + str(dd * aa) + str(dd * cc)
                    if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                        if int(temp) >= maxanswer:
                            maxanswer = int(temp)
                            print aa, bb, cc, dd, maxanswer
                    temp = str(dd * bb) + str(dd * cc) + str(dd * aa)
                    if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                        if int(temp) >= maxanswer:
                            maxanswer = int(temp)
                            print aa, bb, cc, dd, maxanswer
                    temp = str(dd * cc) + str(dd * bb) + str(dd * aa)
                    if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                        if int(temp) >= maxanswer:
                            maxanswer = int(temp)
                            print aa, bb, cc, dd, maxanswer
                    temp = str(dd * cc) + str(dd * aa) + str(dd * bb)
                    if temp.count("0") == 1 and temp.count("1") == 1 and temp.count("2") == 1 and temp.count("3") == 1 and temp.count("4") == 1 and temp.count("5") == 1 and temp.count("6") == 1 and temp.count("7") == 1 and temp.count("8") == 1 and temp.count("9") == 1:
                        if int(temp) >= maxanswer:
                            maxanswer = int(temp)
                            print aa, bb, cc, dd, maxanswer
