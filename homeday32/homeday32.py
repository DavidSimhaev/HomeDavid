from time import perf_counter, sleep
from threading import Thread



def waiter(n):
    print(f'thread {n} started')
    sleep(4)
    print(f'thread {n} ended ')



def main():
    listthreads =[]
    for i in range(10):
        listthreads.append(i)
    threads = [Thread(target=waiter,args=(n,)) for n in listthreads ]
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join() 
    
    
    
    
start_time = perf_counter()

main()

end_time = perf_counter()

print(f"Time taken: {end_time-start_time: 0.2f} seconds")    
