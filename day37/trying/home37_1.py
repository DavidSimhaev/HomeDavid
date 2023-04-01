import random
def coloda():
    nums = [2,3,4,5,6,7,8,9,10,"Валет", "Дама", "Король", "Туз"]
    kinds = ["Пики","Буби", "Крести", "Череви"]
    for x in kinds:
        for y in nums:
            yield(x,y)


l = [ x for x in coloda()]

rlist = []
for x in range(len(l)-1, -1, -1):
    k = random.randint(0,x)
    rlist.append(l.pop(k))
    
print(rlist)

