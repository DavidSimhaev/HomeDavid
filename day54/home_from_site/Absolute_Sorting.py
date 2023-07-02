import re
def checkio(values: list) -> list:
    values_str = "".join(str(values))
    res_str = r"[0-9]+"
    pozitiv_numbers = re.findall(res_str, values_str)
    res = list(map(lambda x: int(x) , pozitiv_numbers))
    res.sort()
    minus = []
    for index in range(len(values)):
        if values[index] < 0:
            minus.append(abs(values[index]))
    pack_res = []
    for elem in values:
        for index in range(len(res)):
            if elem < 0:
                b = int(str(elem)[1::])
                if res[index] == b:
                    res[index] = int("-"+str(b)) 
            else:
                continue
    return res
            
                  
            
            
    print()


print("Example:")

# These "asserts" are used for self-checking
print(checkio([-20, -5, 10, 15])) == [-5, 10, 15, -20]
print(checkio([1, 2, 3, 0])) == [0, 1, 2, 3]
print(checkio([-1, -2, -3, 0])) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")