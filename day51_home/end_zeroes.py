def end_zeros(zeroes: int) -> int:
    zeroes = str(zeroes)
    l = []
    for index in range(len(zeroes)):
        if zeroes[index] == "0":
            l.extend(zeroes[index])
        else:
            l.clear()
    return len(l)
        
            
        


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
print(end_zeros(0)) == 1
print(end_zeros(1)) == 0
print(end_zeros(10)) == 1
print(end_zeros(101)) == 0
print(end_zeros(245)) == 0
print(end_zeros(100100)) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")