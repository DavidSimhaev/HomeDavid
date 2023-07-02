def replace_first(items: list):
    if items == []:
        return []
    t = items.pop(0)
    items.append(t)
    return items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

print(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
print(replace_first([1])) == [1]
print(replace_first([])) == []
