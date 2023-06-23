def is_majority(items: list[bool]) -> bool:
    t = 0
    f = 0
    for index in range(len(items)):
        if items[index] == True:
            t += 1
        elif items[index] == False:
            f += 1
    if t == f:
        return False
    elif t > f:
        return True
    elif t < f:
        return False
    
print("Example:")

# These "print(s" are used for self-checking
print( is_majority([True, True, False, True, False])) == True
print( is_majority([True, True, False])) == True
print( is_majority([True, True, False, False])) == False
print( is_majority([True, True, False, False, False])) == False
print( is_majority([False])) == False
print( is_majority([True])) == True
print( is_majority([])) == False
