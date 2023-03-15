from threading import Thread
from time import perf_counter

def replace(filename, substr, new_substr):
    print(f"process {filename}")
    with open(filename, "r", encoding= "utf-8") as f:
        content = f.read()
    content = content.replace(substr, new_substr)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
        
def main():
    filenames = []
    for i in range(1,11):
        filenames.append(f"test{i}.json")
    threads = [ Thread(target=replace,args=(filename, "Отопление", "Жара")) for filename in filenames]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
        
        
        
start_time = perf_counter()

main()

end_time = perf_counter()


print(f"Time taken: {end_time-start_time: 0.2f} seconds")