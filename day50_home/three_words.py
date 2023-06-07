def checkio(words: str) -> bool:
    text = words.split()
    l = [] 
    for word in text:
        if word.isdigit():
            l.clear()
        else:
            l.append(word)
        if len(l) == 3:
            return True
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
print(checkio("Hello World hello"))
print(checkio("He is 123 man"))
print(checkio("1 2 3 4"))
print(checkio("bla bla bla bla"))
print(checkio("Hi"))