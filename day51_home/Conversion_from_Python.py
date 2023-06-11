def to_camel_case(name: str) -> str:
    res = ""
    for index in range(len(name)):
        if index== 0:
            res += name[0].upper()
        elif name[index] == "_":
            continue
        elif name[index-1] == "_":
            res += name[index].upper()
        else:
            res += name[index]
    return res
        


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
print(to_camel_case("my_function_name")) == "MyFunctionName"
print(to_camel_case("i_phone")) == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")