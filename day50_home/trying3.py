g = {"Вася": 2, "Петя": 3}

g["all_money"] = 909090

print(g)

def d(password):
    num = "1234567890"
    if len(password) > 6:
        pas = "password"
        g = password.lower()
        if pas in password or pas in password.lower():
            return False
        for i in range(len(password)):
            if len(password) > 9:
                return True
            if password[i] in num:
                boolcheck =  0
                for index in range(len(password)):
                    try:
                        int(password[index])
                    except:
                        boolcheck +=1
                        
                if boolcheck != len(password):
                    if boolcheck == 0:
                        return False
                    return True 
                else:
                    return False
                
    else:
        return False
                
            
g= "PASSWORD12345"
print(d(g))


l = []

    
go = "password"

