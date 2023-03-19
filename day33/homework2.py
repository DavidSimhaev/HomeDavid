""" 1 Создать класс (наследник потока) который в потоке будет читать файл и считать количество слов
сделайте так что этот класс запускается start и основной  поток приложения продолжает выводить на экран данные просто какие то выводы """

from threading import Thread
from time import sleep

class MyOwnThread(Thread):
    def __init__(self, limit):
        Thread.__init__(self)
        self._limit = limit
        with open("sherlok.txt",encoding="utf-8") as f:
            fulltext = f.read()
            fulltext =  ''.join ([x for x in fulltext if x.isalpha() or x == ' '])
            fulltext = fulltext.lower()
            ls = fulltext.split()
        
        


m.start()
        
