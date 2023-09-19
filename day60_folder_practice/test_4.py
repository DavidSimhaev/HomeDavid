def mysplit(strng):
    #
    # put your code here
    #
    list_res = []
    res= ""
    for index in range(len(strng)):
        if strng[index] == " ":
            if res == "":
                continue
            list_res.append(res)
            res = ""
            continue
        res += strng[index]    
    return list_res

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
