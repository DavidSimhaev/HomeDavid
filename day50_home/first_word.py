def first_word(text: str) -> str:
    
    l = []
    spec =".,"
    t = text
    for index in range(len(text)):
        if text[index] in spec:
            if text[5] == ".":
                t = text.replace(text[5], " ")
                return t.split()[0]    
            t = text.replace(text[index], "")
            
        elif text[0] == " ":
            return t[1]
    return t.split()[0]
        


print("Example:")

print(first_word('Hello.World'))
# These "asserts" are used for self-checking
print(first_word("Hello world"))# == "Hello"
print(first_word(" a word "))# == "a"
print(first_word("don't touch it"))# == "don't"
print(first_word("greetings, friends"))# == "greetings"
print(first_word("... and so on ..."))# == "and"
print(first_word("hi"))# == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")