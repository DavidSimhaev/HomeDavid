

def zero():
    res = "*** * * * * * * * * * * *** "
    return res


def process():
    list = [zero(), zero(), zero(),zero(), zero(), zero()]
    for l in list:
        print(len(l))
    print(list)
    index= 0
    res = ""
    next_st = False
    
    for number in range(len(list)):
        
        
        
        res+= " ".join([list[number+x][0:3] for x in range(len(list))])+ "\n"
        
        if len(list) % 2 == 0:
            val = 1
        else:
            val =  0 
        res += "\n".join([list[number+x][4:len(list)] for x in range(len(list))])
        
        print(len("*** *** *** *** *** ***"))
        res+= "\n"+" ".join([list[number+x][0:3] for x in range(len(list))])
        
        return res
        
                
                #res+= "\n" + list[number][sym+1:15]
                #res+= "\n"+ " ".join([list[number+x][sym-3:sym] for x in range(len(list))])
                
            #if next_st:
            #res+= "\n".join([list[number+x][sym+1:sym] for x in range(len(list)) ])
                
        return res
     
            
            
print(process())
        