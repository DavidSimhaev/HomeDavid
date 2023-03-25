from datetime import datetime
import random
from threading import Thread
from time import sleep
"""
2 Создайте класс котоый будет генерировать массив из 10_000_000 случайных чисел и писать в файл имя которого вы предложите
запустите три таких потока 
"""

class MyOwnThread(Thread):
    
    def __init__(self, filename):
        Thread.__init__(self)
        self.filename = filename

    def run(self) -> None:
        r = [random.randint(1,1000) for _ in range(1_000_000) ] 
        with open(self.filename, "w") as shfile:
            shfile.write(str(r))
            
            
l = []
for i in range(1,4):
    l.append(MyOwnThread(f"new_file{i}.txt"))
    
for i in range(3):
    l[i].start()
    
for i in range(3):
    l[i].join()
    
    
with open("new_file1.txt","r") as f:
    h = f.read()