def middle(text: str) -> str:
    len_text = len(text)
    if len_text % 2 == 0:
        return text[len_text//2-1]+ text[len_text//2]
    else:
        return text[len_text//2]
        
    


print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
print(middle("example")) == "m"
print(middle("test")) == "es"
print(middle("papapa"))
print(middle("letters")) 


print("The mission is done! Click 'Check Solution' to earn rewards!")