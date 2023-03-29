"""
Создаем итератор из range
numbers = iter(range(1,10000000))
print(200 in numbers)
print(200 in numbers)
объяснить результат

создайте функцию бесконечности 
infinite(list, tries)
for x in infinite([1,2,3], 2):
   print(x)

1 2 3 1 2 3

есть генератор
def show_letters(some_str):
    clean_str = ''.join(letter for letter in some_str if letter.isalpha())
        yield symbol

Реадизуйте генератор колоды карт (52)
    2 Пик
    3 Пик
    ...
"""

def infinite(list, tries):
    
    tries +=1
    list.extend(list)
    
    
    if tries == 3:
        
        return print(list)  
    return infinite(list, tries)

infinite([1,2,3],1)


def show_letters(some_str):
    clean_str = ''.join(letter for letter in some_str if letter.isalpha())
    print(f"Кол букв{len(clean_str)}")


show_letters("Что оптимизировать?")