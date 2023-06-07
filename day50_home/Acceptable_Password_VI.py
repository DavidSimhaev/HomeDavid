# Taken from mission Acceptable Password IV
# Taken from mission Acceptable Password III
# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    # your code here
    num = "1234567890"
    

    
    
    if len(password) > 6:
        pas = "password"
        if pas in password or pas in password.lower():
            return False
        
        l=[]
        for i in range(len(password)):
            
            if len(set(password)) < 3:
                return False 
            
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
                       


print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
print(is_acceptable_password("short"))
print(is_acceptable_password("short54"))
print(is_acceptable_password("muchlonger"))
print(is_acceptable_password("ashort"))
print(is_acceptable_password("muchlonger5"))
print(is_acceptable_password("sh5"))
print(is_acceptable_password("1234567"))
print(is_acceptable_password("12345678910"))
print(is_acceptable_password("password12345"))
print(is_acceptable_password("PASSWORD12345"))
print(is_acceptable_password("pass1234word"))
print(is_acceptable_password("aaaaaa1"))
print(is_acceptable_password("aaaaaabbbbb"))
print(is_acceptable_password("aaaaaabb1"))
print(is_acceptable_password("abc1"))
print(is_acceptable_password("abbcc12"))
print(is_acceptable_password("aaaaaaabbaaaaaaaab"))

print("The mission is done! Click 'Check Solution' to earn rewards!")