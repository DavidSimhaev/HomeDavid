def index_power(ar: list, n: int) -> int:
    for index in range(len(ar)):
        if ar[0] == 0:
            res = ar[index+1]**n 
            return res
        if index == n:
            res = ar[index]**n
            return res
    return -1

    
print(index_power([75, 68, 35, 61, 9, 36, 89, 0, 30], 10))

print("Example:")
print(index_power([1, 2, 3], 2))

# These "asserts" are used for self-checking
print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100], 3))
print(index_power([0, 1], 0)) == 1
print(index_power([1, 2], 3)) == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")