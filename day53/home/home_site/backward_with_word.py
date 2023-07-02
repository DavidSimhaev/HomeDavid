import re
def backward_string_by_word(text: str) -> str:
    text = re.split(r'(\s+)', text)
    l = []
    for index in range(len(text)):
        l.append(text[index][::-1])
    res = "".join(l)
    return res


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
print(backward_string_by_word("")) == ""
print(backward_string_by_word("world")) == "dlrow"
print(backward_string_by_word("hello world")) == "olleh dlrow"
print(backward_string_by_word("hello   world")) == "olleh   dlrow"
print(backward_string_by_word("welcome to a game")) == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")


