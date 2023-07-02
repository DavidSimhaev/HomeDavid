def remove_all_after(items: list[int], border: int):
    res  = []
    for index in range(len(items)):
        if items[index] == border:
            res.append(items[index])
            break
        res.append(items[index])
    return res


print("Example:")

# These "asserts" are used for self-checking
print(list(remove_all_after([1, 2, 3, 4, 5], 3))) == [1, 2, 3]
print(list(remove_all_after([1, 1, 2, 2, 3, 3], 2))) == [1, 1, 2]
print(list(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2))) == [1, 1, 2]
print(list(remove_all_after([1, 1, 5, 6, 7], 2))) == [1, 1, 5, 6, 7]
print(list(remove_all_after([], 0))) == []
print(list(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))) == [7]

print("The mission is done! Click 'Check Solution' to earn rewards!")
