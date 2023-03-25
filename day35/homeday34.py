

def test_decorator(func):
    def wrapper(x ,y, namefile):
        print("----НАЧАЛО ФУНКЦИИ ДЕКОРАТОРА---")
        func(x ,y, namefile)
        print("----ЗАВЕРШЕНИЕ ФУНКЦИИ ДЕКОРАТОРА---")
    return wrapper

def some_func(x , y, namefile):
    while x != y:
        x+=1
        print(f"x = {x}, y = {y}")
        with open(namefile, "w", encoding= "utf8") as f:
            f.write(f"x = {x}, y = {y}")

test = test_decorator(some_func)
test(2,50, "TEST")