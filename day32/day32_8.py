from logging import info, basicConfig, INFO
from threading import Thread
from time import sleep

def theread_function(name):
    info(f"Thread {name} starting")
    sleep(4)
    info(f"Thread {name} stopped")
    
format = "%(asctime)s: %(message)s"

basicConfig(format=format, level=INFO, datefmt="%h:%M:%S")

threads = []

for index in range(3):
    info(f"Main : create and start thread{index}")
    x = Thread(target=theread_function, args=(index, ))
    threads.append(x)
    x.start()
    
for index, thread in enumerate(threads):
    info(f"Main joining thread {index}")
    thread.join()
    info(f"Main - thread---- {index} done")