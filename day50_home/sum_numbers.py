
def sum_numbers(text: str) -> int:
    list_integrs = []
    ready = []
    for index in range(len(text)):
        num = "1234567890"
        if text[index] in num:
            list_integrs.append(text[index])
            try:
                strjoin = "".join(list_integrs)
            except:
                pass
            try:
                if text[index+1] == " ":
                    full_int = int(strjoin)
                    strjoin = ""
                    list_integrs.clear()
                    ready.append(full_int)
            except:
                full_int = int(strjoin)
                list_integrs.clear()
                ready.append(full_int)
    
    return sum(ready)
            
                
        
print("Example:")

print(sum_numbers("5 plus 6 is"))
print(sum_numbers(""))
# These "asserts" are used for self-checking
print(sum_numbers("who is 1st here"))
print(sum_numbers("my numbers is 2"))
print((sum_numbers("This 1845 and 1910 year")))

