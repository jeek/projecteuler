print len([i ** j for i in xrange(1, 10) for j in xrange(1, 22) if len(str(i ** j)) == j])
