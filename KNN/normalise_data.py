def normalise_data(vector):
    vacation = []
    credit = []
    salary = []
    property_ = []
    
    for y in vector:
        a,b,c,d=y[2]
        vacation.append(a)
        credit.append(b)
        salary.append(c)
        property_.append(d)
    
    normalise = lambda vec,min_,max_ : [(f-min_)/(max_-min_) for f in vec]
    
    vacation=normalise(vacation,min(vacation),max(vacation))
    
    credit = normalise(credit,min(credit),max(credit))
    
    salary = normalise(salary,min(salary),max(salary))
    
    property_ = normalise(property_,min(property_),max(property_))
    
    index = 0
    
    for l in vector:
        l[2]=[vacation[index],credit[index],salary[index],property_[index]]
        index+=1
        
    return vector