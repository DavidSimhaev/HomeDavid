from datetime import datetime

def logger(filename):
    def decor(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                with open(filename,"a", encoding= "utf-8") as file:
                    file.write(f"{func.__name__} {datetime.now()} : {result}\n")
            except Exception as ex:
                print(str(ex))
            return result
        return wrapper
    return decor

    
@logger("Test_home34.txt")
def some(x,y,z):
    return(x,y,z)

some("Я рабочая функция",[i for i in range(1,50)],"Ещё один агрумент")