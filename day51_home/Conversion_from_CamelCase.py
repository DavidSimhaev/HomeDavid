def from_camel_case(name: str) -> str:
    res = ""
    for index in range(len(name)):
        if name[index].isupper():
            if name[index] == name[0]:
                res += name[index].lower()
                continue
            else:
                res += "_" + name[index].lower()
        else:
            res += name[index]    
    return res
        


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
print(from_camel_case("MyFunctionName")) == "my_function_name"
print(from_camel_case("IPhone")) == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
