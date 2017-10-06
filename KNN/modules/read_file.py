def read_file(arff_file,file_):
    global arff

    load=arff.load
    
    for row in load(arff_file):
        file_.append(
                
            [ 
                row['Type'],
                row['LifeStyle'],
                map(float,[row['Vacation'],row['eCredit'],row['salary'],row['property']]),
                row['label']
            ]
            
        )
        
    return file_