def cut_sentence(line: str, length: int) -> str:
    word = 0
    res = ""
    for index in range(len(line)):
        if line[index] == " ":
            word += 1
        if index == length:
            line = line.split()
            for text in range(0, line.index(line[word])):
                res += line[text] + " "
            return res[:len(res)-1] + "..."
    return line
            
             


# These "asserts" are used for self-checking
print(cut_sentence('Hi my name is Alex', 10))
print( cut_sentence("Hi my name is Alex", 4)) == "Hi..."
print(cut_sentence("Hi my name is Alex", 8))  == "Hi my..."
print(cut_sentence("Hi my name is Alex", 9)) 
print(cut_sentence("Hi my name is Alex", 18)) 
