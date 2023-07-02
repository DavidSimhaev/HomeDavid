def stock_profit(stock: list[int]) -> int:
    l =[]
    start_program = False
    for index in range(len(stock)):
        try:  
            if stock[index] < stock[index+1]:
                l.append(stock[index])
                start_program = True
            elif start_program:
                if min(l) < stock[index]:
                    l.append(stock[index])
            else:
                l.clear()
                start_program = False
        except:
            if start_program:
                if min(l) < stock[index]:
                    l.append(stock[index])
    if len(l) == 0:
        return 0
    res = max(l)-min(l)
    return res
              


print("Example:")
print(stock_profit([60, 50, 51, 52, 40])) == 2

# These "asserts" are used for self-checking
print(stock_profit([2, 3, 4, 5])) == 3
print(stock_profit([3, 1, 3, 4, 5, 1])) == 4
print(stock_profit([4, 3, 2, 1])) == 0
print(stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4])) == 4
print(stock_profit([1, 1, 1, 2, 1, 1, 1])) == 1
print(stock_profit([4, 3, 2, 1, 2, 1, 2, 1])) == 1
print(stock_profit([1, 1, 1, 1])) == 0