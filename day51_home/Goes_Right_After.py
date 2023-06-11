"""В данном слове вам нужно проверить, идет ли один символ только сразу за другим.

Случаи, которых вам следует ожидать при решении этой задачи:

одного из символов нет в данном слове - ваша функция должна возвращать значение False;
любой символ появляется в слове более одного раза - используйте только первый;
два символа совпадают - ваша функция должна возвращать значение False;
условие чувствительно к регистру, что означает, что 'a' и 'A' - это два разных символа.
Входные данные: три аргумента. Первый - это заданная строка, второй - символ, который должен идти первым, а третий - символ, который должен идти после первого.

Вывод: значение bool.

Примеры:"""

def goes_after(word: str, first: str, second: str) -> bool:
    l = []
    for index in range(len(word)):
        if word[index] == first:
            l.append(word[index])
            try:
                if word[index+1] == second:
                    return True
                else:
                    l.clear()
            except:
                pass    
    return False

print(goes_after('transport', 'r', 't'))
print("Example:")
print(goes_after("world", "w", "o"))

# These "asserts" are used for self-checking
"""print(goes_after("world", "w", "o"))
print(goes_after("world", "w", "r"))
print(goes_after("world", "l", "o"))
print(goes_after("panorama", "a", "n"))
print(goes_after("list", "l", "o"))
print(goes_after("", "l", "o")) """
print(goes_after("list", "l", "l")) 
print(goes_after("world", "d", "w"))
print(goes_after("Almaz", "a", "l"))

print("The mission is done! Click 'Check Solution' to earn rewards!")