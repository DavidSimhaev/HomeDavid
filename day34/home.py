"""
1 есть очередь - потоков клиентов ночного клуба (300) их пропускают барьером по 15 человек
    на столе бочонок пива одновременно налить может только один человек (наливается пиво 1 секунду)
    человек решает хочет или не хочет пива с вероятностью 50 процентов
2 Придумайте сами ситуацию для использования класса таймер     
    """
    


from threading import Barrier, Thread
from time import sleep, time

br = Barrier(3)
club = []

def f1(x):
    
    print("Первый вход!")
    
    sleep(1)
    
    club.append(x+2)
    br.wait()
    
def f2(x):
    print("Второй вход!")
   
    sleep(2)
    club.append(x+2)
    br.wait()

t1 = [Thread(target=f1, args=(i,)) for i in range(1,150)]
t2 = [Thread(target=f2, args=(i,)) for i in range(1,150)]

print(club)
br.wait()


print("Result: ", sum(club))



