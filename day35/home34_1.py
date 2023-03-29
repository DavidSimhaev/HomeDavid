def repeater(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
           
            for i in range(4):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator
    
    
@repeater(4)
def some(x,y, p = 2):
    print(x+y+p)
    return(p+x-y)

some(2,3)

#p = repeater(10)(some)(2,3,p=4)