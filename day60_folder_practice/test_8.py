def Polindrom(polindrom):
    polindrom = "Ten animals I slam in a net"
    polindrom = polindrom.replace(" ", "")
    if polindrom.lower() == polindrom.lower()[::-1]:
        return True 
    else:
        return False
def Anagram(anagram):
    l = []
    anagram = anagram.lower().replace(" ", "")
    for sym in anagram:
        l.append(sym)
    res = []
    for sym in l:
        res.append(l.count(sym))
    for i in res:
        if i > 1:
            return "Not anagrams"
        else:
            continue
    return "Anagrams"
print(Anagram("Silent"))

def check(arg_one, arg_two):
    arg_one = arg_one.lower().replace(" ", "")
    arg_two = arg_two.lower().replace(" ", "")
    continue_process = True
    for arg1 in arg_one:
        if continue_process:
            if arg1 in arg_two:
                continue
            else:
                continue_process = False
        else:
            return "No"
    return "Yes"

print(check("Abc" , "Cba"))