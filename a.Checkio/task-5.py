def best_stock(data: dict[str, float]) -> str:
    
    max_val = max(list(map(lambda x: data[x] ,data.keys())))
    res = [i for i in data.keys() if data[i] == max_val]
    return res[0]
    

print("Example:")
print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))# == "ATX"
print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}))# == "TASI"

print("The mission is done! Click 'Check Solution' to earn rewards!")
