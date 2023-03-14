from time import perf_counter
import json

def replace(filename, substr, new_substr):
    print(f"process {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        content = json.load(f)
    content = content.replace(substr, new_substr)
    
    with open(filename, "w") as f:
        f.write(content)
        
        
def main():
    filenames = []
    for i in range(1,11):
        filenames.append(f"test{i}.json")
        
    for filename in filenames:
        replace(filename, "Отопление", "Жара")
        
        
        
start_time = perf_counter()

main()

end_time = perf_counter()


print(f"Time taken: {end_time-start_time: 0.2f} seconds")