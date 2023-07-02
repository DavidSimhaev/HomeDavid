import re


def compress(items: list[int]):
    l = []
    for index in range(len(items)):
        try:
            if items[index] == items[index+1]:
                continue
            else:
                l.append(items[index])  
        except:
            l.append(items[index])
    return l


print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

# These "asserts" are used for self-checking
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0]))) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
print(list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1]))) == [1, 2, 1]
print(list(compress([7, 7]))) == [7]
print(list(compress([]))) == []
print(list(compress([1, 2, 3, 4]))) == [1, 2, 3, 4]
print(list(compress([9, 9, 9, 9, 9, 9, 9]))) == [9]
print(list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9]))) == [9, 0, 9]

print("The mission is done! Click 'Check Solution' to earn rewards!")
