def all_the_same(elements) -> bool:
    if len(set(elements))== 1:
        return True
    else:
        if elements == []:
            return True
        return False


print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
print(all_the_same([1, 1, 1])) == True
print(all_the_same([1, 2, 1])) == False
print(all_the_same([1, "a", 1])) == False
print(all_the_same([1, 1, 1, 2])) == False
print(all_the_same([])) == True
print(all_the_same([1])) == True