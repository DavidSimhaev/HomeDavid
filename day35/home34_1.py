def repeater(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("Fkjk")
            for i in range(n-1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator
    
    
@repeater(2)
def some(x,y, p = 2):
    print(x+y+p)
    return(p+x-y)

some(2,3)

#p = repeater(10)(some)(2,3,p=4)