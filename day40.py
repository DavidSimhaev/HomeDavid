lists = [
    [1,2,3,4,5,6],
    ["a","b", "c","d"],
    [1,1,1]
]

res = [i for i in lists if all([isinstance(item, int) for item in i ]) and sum(i)<4]

print(res)

a = list(filter(lambda x: all([isinstance(item, int) for item in x ]) and sum(x)<4 ,lists))

print(a)