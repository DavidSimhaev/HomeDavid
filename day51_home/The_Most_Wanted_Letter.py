def checkio(text: str) -> str:

    text = text.lower()
    l = []
    alfabet = list(map(chr, range(97, 123)))
    for index in range(len(text)):
        m = all([x == 1 for x in text[index]])
        if m:
            print()

            
            
        
    


print("Example:")
#print(checkio("Hello World!"))

# These "asserts" are used for self-checking

print(checkio("One")) == "e"
print(checkio("Oops!")) == "o"
print(checkio("AAaooo!!!!")) == "a"
print(checkio("abe")) == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")