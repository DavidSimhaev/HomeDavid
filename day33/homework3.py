""" 2 Создайте класс котоый будет генерировать массив из 10_000_000 случайных чисел и писать в файл имя которого вы предложите
запустите три таких потока 
 """
from threading import Thread, Lock
from time import sleep
import random 
import concurrent
from concurrent import futures

lock = Lock()
stop_thread = False

def func(number, name):
    while True:
        print(f"Имя потока: {name}, Число {number} ")
        if lock.acquire(blocking = True, timeout=3):
            if stop_thread is True:
                lock.release()
                break
            lock.release()
    
        sleep(0.5)
g = [random.randrange(1,100000) for i in range(0, 10000)]

l1 = [ Thread(target=func, args=(x, 1)) for x in g ]
l2 = [ Thread(target=func, args=(x, 2)) for x in g ]
l3 = [ Thread(target=func, args=(x, 3)) for x in g ]

threads =[]



for i in l1:
    threads.append(i)
for i in l2:
    threads.append(i)
for i in l3:
    threads.append(i)

for t in threads :
    t.start()
for t in threads: 
    t.join()

print('done')