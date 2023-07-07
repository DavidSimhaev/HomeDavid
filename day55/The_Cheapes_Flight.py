def cheapest_flight(costs: list, a: str, b: str) -> int:
    def func_sort_list(list, start_end ):
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
    direction = False
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
    dict = {}
    dict_check_list = {}
    check = 1
    c = False
    direction = False
    check_end = False
    p = 0
    g = 0
    dict[f"list {check}"] = []
    dict_check_list[f"list {g}"] = []
    
    
    def check_list(elem_ind):
        l = []
        for key in dict:
            for index_list in dict[key]:
                if type(index_list) == tuple:
                    for elem in index_list:
                        if elem == elem_ind:
                            l.append(elem_ind)
                            continue
                else:
                    l.append(index_list)
        return l
    
    for index in range(len(res)):
        for elem_index in range(len(res[index])):            
        
            if res[index][elem_index] == a and res[index][elem_index+1] == b or res[index][elem_index] == b and res[index][elem_index+1] == a:
                break
        
            if direction == True:
                for key in dict:
                    res_center = list(map(lambda x: check_list(x), dict[key][-1]))
                    check_end = True
                    direction = False
                    c = True
                    break
            if c == True:
                c = False
                break
            if check_end == True:
                for index_r in range(len(res_center)):
                    if res_center[index_r][-1][1] == res[index][elem_index]:
                        res_center[index_r].append(res[index])
                price = []     
                result = []   
                for index_r in range(len(res_center)):
                    price.clear()
                    for ielem in range(len(res_center[index_r])):
                        price.append(res_center[index_r][ielem][2])

                    res_price = sum(price)
                    result.append(res_price)
                index_res = result.index(min(result))
                res = []
                for key in dict:
                    dict[key][-1] = dict[key][-1][index_res]
                    for ind_l in range(len(dict[key])):
                        res.append(dict[key][ind_l][2])
                return sum(res)
            
            if elem_index == 2:
                break
            if res[index][elem_index] == a: 
                if elem_index == 1:
                    x = res[index][elem_index-1]
                    y = res[index][elem_index]
                    res[index][elem_index-1] = y
                    res[index][elem_index] = x 
                    dict[f"list {check}"].append(res[index])
                    break
                    
                elif elem_index == 0:
                    check +=1 
                    dict[f"list {check}"] = []
                    dict[f"list {check}"].append(res[index])
                    break
            
            elif res[index][0] == b:
                x = res[index][elem_index+1]
                y = res[index][elem_index]
                res[index][0] = x
                res[index][1] = y
            for key in dict:
                for _ in range(len(dict[key])):
                    if dict[key][-1][1] == res[index][0]: # Если последний элемент равен следущему рейсу
        
                        dict[key].append(res[index])
                        c = True
                        continue
                try:
                    if dict[key]== []:
                        continue
                    int(res[index][elem_index+1])
                    tuple_check = False
                    if dict[key][-1][0] == res[index][0]:
                        dict[key][-1] = dict[key][-1], res[index]
                        tuple_check = True
                    for key in dict: 
                        if tuple_check == True:
                            break
                        for ind_list_key in range(len(dict[key])):
                            if type(dict[key][ind_list_key]) == tuple:
                                tuple_check = True
                                break
                            if dict[key][ind_list_key][0] == res[index][0] and res[index][1] == b:
                                res_2 = dict[key][ind_list_key-1], res[index]
                                break
                    if tuple_check:
                        direction = True
                    break
                        
                except Exception as ex:
                    pass     
    arg =[]
    check_arg= []         
    try:
        if res_2:
            check +=1 
            dict[f"list {check}"] = res_2
    except:
        pass
    for key in dict:
        arg.clear()
        for ind_l in range(len(dict[key])):
            if dict[key][-1][1] != b:
                continue
            arg.append(dict[key][ind_l][2])
        if arg == []:
            continue
        check_arg.append(sum(arg))
    
    if check_arg == []:
        return 0
    if len(set(check_arg)) == 1:
        return check_arg[0]
    return min(check_arg)
                    

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
print("The mission is done! Click 'Check Solution' to earn rewards!")

print((
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A"))# == 70
)
  
print(cheapest_flight([['A', 'B', 10], ['A', 'C', 20],
                 ['B', 'D', 15],  ['C', 'D', 5],
                 ['D', 'E', 5], ['E', 'F', 10], ['C', 'F', 25]], 'A', 'F'))# == 40

print("The mission is done! Click 'Check Solution' to earn rewards!")

