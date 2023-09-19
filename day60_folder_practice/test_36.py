def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)