# a = a + result a = 5
# 6 11 -> a
# 12 17->a 
# 17 - 23

from threading import Thread, Lock
from time import sleep

lock = Lock()
stop_thread = False

def ant(number):
    print("Муравей никогда не устает! Начал работать")
    while True:
        print(f"---> МУРАВЕЙ РАБОТАЕТ: {number}")
        lock.acquire()
        if stop_thread is True:
            lock.release()
            break
        lock.release()
        sleep(0.1)
    print("Что то остановило муравья!!!")
    
t = Thread(target=ant, args=(1,))
t1 = Thread(target=ant, args=(2,))
t.start()
t1.start()
sleep(2)
lock.acquire()
stop_thread = False
print("Stop threads!")
sleep(5)
lock.release()
sleep(5)
lock.acquire()
stop_thread = True
print("Stop threads! 4 секунд на размышления")
sleep(4)
lock.release()

print("Oi!")