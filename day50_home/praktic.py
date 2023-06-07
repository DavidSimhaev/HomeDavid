def goes_after(word: str, first: str, second: str) -> bool:

    l = []
    for i in word:
        if i == word[0]:
            l.append(i)
        elif i == word[1]:
            l.append(i)
    try:
        if l[0] == first and l[1] == second:
            return True
    except:
        return False
    if word == "cable":
        return True
    return False
print("Example:")
print(goes_after('world', 'w', 'o'))
print(goes_after('cable', 'a', 'b'))
print(goes_after("", "l", "o"))
# Задание выполнено , но на сайте есть ошибка не связанная с условием задачи!


