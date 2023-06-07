def beginning_zeros(a: str) -> int:
    zero_index = 0
    for index in range(len(a)):
        if a[index] == "0":
            zero_index +=1
            res = "0" * zero_index
            continue
        elif a[0] != "0":
            return 0
        return len(res)
    return len(res)
        
    


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking

print(beginning_zeros("0000"))

print("The mission is done! Click 'Check Solution' to earn rewards!")