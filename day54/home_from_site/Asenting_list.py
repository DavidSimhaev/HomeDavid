def is_ascending(items: list[int]) -> bool:
    if items == []:
        return True
    for index in range(len(items)):
        try:
            if items[index] < items[index+1]:
                continue
            else:
                return False
        except:
            return True


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

# These "asserts" are used for self-checking
print(is_ascending([-5, 10, 99, 123456])) == True
print(is_ascending([99])) == True
print(is_ascending([4, 5, 6, 7, 3, 7, 9])) == False
print(is_ascending([])) == True
print(is_ascending([1, 1, 1, 1])) == False
print(is_ascending([1, 3, 3, 5])) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")