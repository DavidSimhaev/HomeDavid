



def is_even(num: int) -> bool:
    # your code here
    if num%2:
        a = num%2
        return False
    return True

print(is_even(3))

print("----")
v = "vasia"
d = [i for i in reversed(v)]
e = "".join(d)
print(e)

b = list(map(chr, range(97, 123)))
print(b)
def c(masiv):
    d = input("Введите слово: ")
    for i in d:
        if i in masiv or i in str(masiv).upper():
            return str(d.split(" ")[0])
        return False
print(c(b))
#assert first_word("Hello world") == "Hello"
##assert first_word("a word") == "a"
#assert first_word("greeting from CheckiO Planet") == "greeting"
#assert first_word("hi") == "hi"

def num(n):
    return len(str(n))
    
f = int(input("Введите число: "))
print(num(f))


def pas(pasw):
    if len(pasw)> 6:
        g = [1,2,3,4,5,6,7,8,9,0]
        if g in pasw:
            return False
        else: 
            return True

f = input("Придумайте пароль")
print(pas(f))