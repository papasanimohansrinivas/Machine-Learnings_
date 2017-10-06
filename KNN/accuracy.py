def accuracy(result,validation):
    
    r1 = len(result)
    
    matches = lambda v1,v2,r1: [1 if v1[r]==v2[r] else 0 for r in xrange(r1)]

    print matches(result,validation,r1)    
    
    return float(matches(result,validation,r1).count(1))/len(result)*100
