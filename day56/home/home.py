"""1 Создать класс мобильник - создать несколько экземпляров со случакйными номерами,
в классе конструктор сохраняет номер телефона
метод включить - печатает номер - "включен" и метод выключить - печатает выкелючен
включать выключать 
"""
import datetime
import random
import time
class telephon:
    def __init__(self, number) -> None:
        self.number = number
    
    def on(self):
        print(f"Номер: {self.number} - Включен")
    
    def off(self):
        print(f"Номер: {self.number} - Выключен")
    
def number_r():
    number_num = "+9725"
    l = []
    res = random.randrange(2,6)
    l.clear()
    number_num += str(res)
    for _ in range(8):
        res = random.randrange(9)
        number_num += str(res)
    return number_num
  
tel1 = telephon(number_r())
tel2 = telephon(number_r())
tel3 = telephon(number_r())
for x in tel1,tel2, tel3:
    x.on()
"""
2 Создать класс временного интервала
    методы для сложения? вычитания? умножения на число
    при создании должен принимать параметры часы минуты секунды
    метод предсавления __str__ HH:MM:SS"""


class time_counter():
    def __init__(self, H, M) -> None:
        
        self.H = H
        self.M = M
    
    def itnerval(self):
        while True:
            time.sleep(1)
            if datetime.datetime.now().hour != self.H or datetime.datetime.now().minute != self.M:
                print(datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second)
            else:
                return print("Программа остановилась")

time1= time_counter(9, 0 )           

time1.itnerval()            
        

