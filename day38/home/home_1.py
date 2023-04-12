import random
import pandas as pd
import numpy as np
# 1 конвертировать серию в список
s = pd.Series([100, 200, 300, 400, 500])
d = list(s)
print(d,"Результат преобразования 1")

# 2 есть словарь {'a':100, 'b':200, 'c':300, 'd':400} -----   конвертировать в серию

s = {'a':100, 'b':200, 'c':300, 'd':400}
d = pd.Series(s)
print(d,"Результат преобразования 2")

# 3 сделайте numpy array - сконвертируйте в серию
def random_array():
    l = [random.randint(1,5) for _ in range(4) ]
    return l

s = np.array(random_array())
print(s, "Массив нампи")

d = pd.Series(s)
print(d, "Результат преобразования 3")

# 4 сконвертировать серии списков в одну серию
d = pd.Series([random_array(),random_array(),random_array(),random_array()])
 # Мой неправильный вариант
print(d)
s = pd.Series(d)
print(s)

# Мой правильный вариант
s = s.apply(pd.Series).stack().reset_index(drop=True)
print(s)

# 5 напишите сравнение двух серий (числовых)
def random_arr():
    l = [random.randint(1,2) for _ in range(10) ]
    return l

d = pd.Series(random_arr())
s = pd.Series(random_arr())

print(d)
print(s)
    
print(d==s)

#6 найдите где количетсво попыток меньше 1 и оценка больше 15
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, -3, 2, -3, 1, 1, -2, -1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
exams = pd.DataFrame(exam_data, index= labels)
print(f" Кол-во попыток меньше 1: {len(exams[exams.attempts < 1])}\n Оценка больше 15: {len(exams[exams.score > 15])}")

#7 найдите макс и мин оценки
print(f"Макс оценка: {exams.score.max()}")
print(f"Мин оценка: {exams.score.min()}")
#8 макс кол-во попыток
print(f"Макс кол-во попыток: {exams.attempts.max()}")

#9 Удалить колонку
del exams["qualify"]
print(exams)
#10 добавить колонку 
exams["newcolonka"] = 1
print(exams)
#11 Везде поставить yes в attemtps
exams["attempts"] = "yes" 
print(exams)
#12 попробуйте функцию iterrows() для обхода циклом датафрейма (две переменных индекс и сама строка)
row = exams.iterrows()
print(next(row))
print(next(row))
print(next(row))
