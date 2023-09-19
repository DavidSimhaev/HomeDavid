def double_step(n):
    for i in range(0, 2*n):
        yield i

for v in double_step(5):
    print(v, end=" ")


def Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

print(list(Fib(10)))

new_list = []
for element in range(3):
    if element % 2 != 0:
        new_list.append(10 ** element)



import os

try:
    stream = open("c:/users/user/Desktop/file.txt", "rt")
    # Actual processing goes here.
    stream.close()
except IOError as exception:
    print("The file could not be opened:", os.strerror(exception.errno))

import os

try:
    stream = open("TEST.txt", "rt")
    character = stream.read(2)
    while character != "":
        print(character, end="")
        character = stream.read(1)
    stream.close()
except IOError as exception:
    print("I/O error occurred: ", os.strerror(exception.errno))


try:
    stream = open("TEST.txt", "rt")
    line = stream.readline()
    while line != "":
        print(line, end="")
        line = stream.readline()
    stream.close()
except IOError as exception:
    print("I/O error occurred:", os.strerror(exception.errno))


try:
    stream = open("newfile.txt", "wt")
    for i in range(100):
        stream.write("*" * 10 + "\n")
    stream.close()
except IOError as exception:
    print("I/O error occurred: ", os.strerror(exception.errno))
    
    
data = bytearray(10)


import os

byte = bytearray(1)
bytes_95 = bytearray(95)
try:
    out_stream = open("file.bin", "wb")
    for i in range(32,127):
        byte[0] = i;
        out_stream.write(byte)
    out_stream.close();
    in_stream = open("file.bin", "rb")
    
    read_in = in_stream.readinto(bytes_95)
    in_stream.close()
    print("\n", read_in,"byte(s) read in")
    for i in range(95):
        print(chr(bytes_95[i]))
except IOError as exception:
    print("I/O error occurred:", os.strerror(exception.errno))




class ASSS(Exception):
    
    def __init__(self, mess) -> None:
        self.atr= mess
        
        
    def __str__(self) -> str:
        return "lalala"
    
    

print("atr" in ASSS.__dict__)