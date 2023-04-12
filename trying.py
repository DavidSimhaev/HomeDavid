import numpy as np

def test_decorator( function_to_decorate ):
    # обертка
    def wrapper ():
        print(f"я decorator1 я съел функцию {function_to_decorate}")
        function_to_decorate()
        
    return wrapper


def test_decorator1(function_to_decorate):
    # обертка
    def wrapper():
        print(f"я decorator2 я съел функцию {function_to_decorate}")
        function_to_decorate()

    return wrapper

@test_decorator
@test_decorator1
def ordinary_method():
    print("я обычный метод или обычная функция")

#ordinary_method()
#test_decorator(ordinary_method)

#ordinary_method()
import numpy as np

arr1 = np.array([1,2,0,3,4])
print (np.log(arr1))