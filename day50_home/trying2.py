def infinite (list,tries):
   l=[x for x in range(1,4)]
   tries=tries-1
   list.extend(l*tries)
   print(list)
     


infinite([1,2,3],2)

print("------")

li = [0, 1, 2, 3]

running = True
def checkio(words: str) -> int:
    
    words = words.split()
    b = 0
    for word in words:
        try:
            int(word)
            b = 0
        except:
            b +=1
            if b == 3:
                return True
    return False
    


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
print(checkio("Hello World hello")) == True
print(checkio("He is 123 man")) == False
print(checkio("1 2 3 4")) == False
print(checkio("bla bla bla bla")) == True
print(checkio("Hi")) == False