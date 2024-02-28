def correct_capital(line: str) -> bool:
    if line.isupper():
        return True
    elif line.istitle():
        return True
    elif line.islower():
        return True
    return False


print("Example:")
print(correct_capital("Checkio"))

# These "asserts" are used for self-checking
print(correct_capital("Checkio"))# == True
print(correct_capital("CheCkio"))# == False
print(correct_capital("CHECKIO"))# == True

print("The mission is done! Click 'Check Solution' to earn rewards!")

def long_repeat(line: str) -> int:
    
    list = []
    counter = 1
    if line == '':
        return 0
    for index in range(len(line)):
        try:
            if line[index] == line[index+1]:
                counter+=1
            else:
                list.append(counter)
                counter = 1
        except IndexError:
            list.append(counter)
    return max(list)


print("Example:")
print(long_repeat("sdsffffse"))

print( long_repeat("sdsffffse")) == 4
print(long_repeat("ddvvrwwwrggg")) == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
