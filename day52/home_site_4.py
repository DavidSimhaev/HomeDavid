def checkio(array: list[int]) -> int:
    l = []
    for index in range(len(array)):
        if index % 2 == 0: # Если четное
            l.append(array[index])
        else:
            continue
    if l == []:
        return 0
    res = sum(l) * array[-1]
    return res

print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
print(checkio([0, 1, 2, 3, 4, 5])) == 30
print(checkio([1, 3, 5])) == 30
print(checkio([6])) == 36
print(checkio([])) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")