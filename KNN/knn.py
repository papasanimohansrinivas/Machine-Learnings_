def KNN(Dtest,Dtrain):
    
    result = []

    import math
    
    similar =  lambda x,y: 1 if x==y else 0
    
    distance = lambda v1: math.sqrt(sum([v**2 for v in v1]))
    
    diff = lambda v0,v2,l : [v0[n]-v2[n] for n in xrange(l)]
        
    top_five = lambda vec : [vec[i][1] for i in xrange(0,5)]
    
    reverse=lambda dict_1,v:{
        v:sorted([key for key in dict_1 if dict_1[key]==v])
    }
        
    from operator import itemgetter
    
    app_ = result.append
    
    for vec in Dtest:
        distances = []
        
        app=distances.append 
        
        for vec_ in Dtrain:
            a=1-similar(vec[0],vec_[0])
            b=1-similar(vec[1],vec_[1])
            c,d,e,f = diff(vec[2],vec_[2],len(vec_[2]))
            app([distance([a,b,c,d,e,f]),vec_[3]])
        
        distances=sorted(distances,key=itemgetter(0))
        
        classes = top_five(distances)
        
        class_ = {
            'C1': classes.count('C1'),
            'C2': classes.count('C2'),
            'C3': classes.count('C3'),
            'C4': classes.count('C4'),
            'C5': classes.count('C5')
        }
        
        v=max(class_.values())
        
        d=reverse(class_,v)
        
        app_(d[v][0])
        
    return result
        