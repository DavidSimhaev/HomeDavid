def checkio(data: list[int]):
    data = sorted(data)
    print(data)
    if len(data) % 2 == 0: # Это четное
        index = len(data) // 2 -1
        res = (data[index] + data[index+1])/2
        return res
    else: # В противном случаи если оно нечетное 
        index = len(data) // 2
        res = data[index]
        return res
        


print("Example:")
print(checkio([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
print( checkio([1, 2, 3, 4, 5])) == 3
print( checkio([3, 1, 2, 5, 3])) == 3
print( checkio([1, 300, 2, 200, 1])) == 2
print( checkio([3, 6, 20, 99, 10, 15])) == 12.5
print( checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) == 5
print( checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3])) == 4.5
print( checkio([33, 56, 62])) == 56
print( checkio([21, 56, 84, 82, 52, 9])) == 54
print( checkio([100, 1, 1, 1, 1, 1, 1])) == 1
print( checkio([64, 6, 92, 7, 70, 5])) == 35.5

print("The mission is done! Click 'Check Solution' to earn rewards!")