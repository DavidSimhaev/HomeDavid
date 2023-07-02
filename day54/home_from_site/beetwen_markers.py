"""You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:"""
b = 0
c = 0
def between_markers(text: str, begin: str, end: str) -> str:
    def iterator_start(elem):
        global b
        for index in range(b, len(begin)):
            if elem == begin[index]:
                b += 1
                return True
            else:
                b = 0
                return False  
    begin_check_start = list(map(lambda x: True == iterator_start(x) , text))
    def iterator_end(elem):
        global c
        for index in range(c, len(end)):
            if elem == end[index]:
                c += 1
                return True
            else:
                c = 0
                return False
    check_end = list(map(lambda x: True == iterator_end(x) , text))
    global b
    global c
    b = 0
    c = 0
    s = 0
    e = 0
    for boll in range(len(begin_check_start)):
        if begin_check_start[boll] == True:
            s +=1
            if s == len(begin):
                index_boll_start = boll
                break
        else:
            index_boll_start = False
            s = 0
    for end_boll in range(len(check_end)): # Если мы прошлись по циклу и не вышли некуда значить нет конца 
        if check_end[end_boll] == True:
            e+= 1
            if e == len(end):
                index_boll_end = end_boll 
                if index_boll_start == False:
                    return text[0:index_boll_end-len(end)+1]
                return text[index_boll_start+1: index_boll_end-len(end)+1]
        else:
            index_boll_end = False
            e = 0
            
    if index_boll_end == False and index_boll_start == False:
        return text
    
    return text[index_boll_start+1::]
        
    
    
        


print("Example:")

print(between_markers("No[/b] hi", "[b]", "[/b]")) == "No"
print(between_markers("No [b]hi", "[b]", "[/b]")) == "hi"
print(between_markers("No hi", "[b]", "[/b]")) == "No hi"
print(between_markers("No <hi>", ">", "<")) == ""

#print("The mission is done! Click 'Check Solution' to earn rewards!")