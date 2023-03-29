def infinite (list,tries):
   l=[x for x in range(1,4)]
   tries=tries-1
   list.extend(l*tries)
   print(list)
     


infinite([1,2,3],2)