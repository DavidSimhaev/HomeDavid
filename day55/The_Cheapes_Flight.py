def cheapest_flight(costs: list, a: str, b: str) -> int:
    def func_sort_list(list, start_end ):
        global stop_step
        q = 0
        for elem in list:
            if elem == start_end:
                return list
            elif start_end == 0:
                if elem != a and elem != b and type(elem) != int:
                    q+=1
                    if q==2:
                        return list
    sort_list_a = list(map(lambda x: func_sort_list(x, a), costs ))
    
    sort_no_name = list(map(lambda x: func_sort_list(x, 0), costs ))
    
    sort_list_b = list(map(lambda x: func_sort_list(x, b), costs ))
    
    res = sort_list_a + sort_no_name + sort_list_b
    d =0
    for _ in range(0,len(res)-d):
        d-= 1
        try:
            res.remove(None)
        except:
            break
    e = 0
    p = 0
    f = 0
    check = False

    res = list(reversed(res))
    for index in range(len(res)):
        if check == True:
            f+=1
        if res[index][0] == a and res[index][1] == b or res[index][0] == b and res[index][1] == a:
            p +=1
            check = True
            if p == 2:
                res.pop(index-f)
                break
    res.reverse()
    
    g = True
    l = []
    res_start = a 
    res_end = b
    for index in range(len(res)):
        for elem_index in range(len(res[index])):
            if g== True:
                if res[index][elem_index] == res_start and res[index][elem_index+1] == res_end or res[index][elem_index] == res_end and res[index][elem_index+1] == res_start  :
                    g = False
                    break
            if res[index][elem_index] == a:
                try:
                    int(res[index][elem_index+1])
                    #[['A', 'D', 20], ['D', 'C', 70], ['A', 'B', 20], ['A', 'C', 40], ['B', 'C', 50]]
                    x = res[index][elem_index-1]
                    y = res[index][elem_index]
                    res[index][elem_index] = x
                    res[index][elem_index-1] = y
                    a = res[index][elem_index]
                    l.append(res[index])
                    
                    break
                except:
                    if index < 2:
                        l.append(res[index][elem_index+1::])
                        a = res[index][elem_index+1]
                        break
                    if res[index][elem_index+1] != res_end:
                        continue
                    l.append(res[index][elem_index+1::])     
            elif elem_index == 2:
                break
            else:
                continue

    def func(index_list):
        for elem in index_list:
            try:
                int(elem)
                return elem
                
            except:
                continue
        return res
    if len(res) <=1:
        return 0
    res = list(map(lambda x: func(x), l))
    return sum(res)
            
#print(
#    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C")) == 70

#print((
#    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A"))# == 70
#)

print((
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    ))#    == 60
)

print(
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F"))# == 0

print(
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    ))
#    == 25      
print(cheapest_flight([['A', 'B', 10], ['A', 'C', 20],
                 ['B', 'D', 15],  ['C', 'D', 5],
                 ['D', 'E', 5], ['E', 'F', 10], ['C', 'F', 25]], 'A', 'F')) == 40

print("The mission is done! Click 'Check Solution' to earn rewards!")

