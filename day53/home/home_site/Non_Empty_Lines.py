import string


def non_empty_lines(text: str) -> int:
    b = 0
    text = text.replace(" ", "")
    if len(text) == 0:
        return 0
    for index in range(len(text)):
        try:
            text[index+1]
        except:
            break
        if text[index] == "\n":
            continue
        if text[index-1] == "\n" and text[index].lower() in string.ascii_lowercase:
            b+=1
    return b
        
            

print("Example:")

# These "asserts" are used for self-checking
print(non_empty_lines("onesimpleline\n")) == 1
print(non_empty_lines("")) == 0
print(non_empty_lines("\nonlyoneline\n")) == 1
print((
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    ))
)
print(non_empty_lines('\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\nNullam ante ligula,\n          \n          fermentum a porta\n            ')) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")