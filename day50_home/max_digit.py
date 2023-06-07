def max_digit(value: int) -> int:
    
    string_int = str(value)
    res = list(string_int)
    for index in range(len(str(string_int))):
        
         
        if string_int[index] == max(res):
            return int(max(res))
        
        
    
    


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
print(max_digit(0))

print(max_digit(52))
print(max_digit(634))