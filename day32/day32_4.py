from threading import Thread
from time import sleep, perf_counter
from solver import solve

mathlist = []

results = []
def mathprocess(values: str, pattern: str):
    result = []
    for x in range(1,101):
         r= solve(values.replace(pattern, str(x)))
         result.append(r)
         print(r)
mathlist.append("sin({x})*{x}")
mathlist.append("cos({x})*{x}")
mathlist.append("{x}*5-{x}*{x}")


for s in mathlist:
    mathprocess(s, "{x}")