from pprint import pprint
import random
import numpy

a = numpy.array([[random.randint(1,100) for i in range(1,4)], [random.randint(1,100) for i in range(1,4)]])
b = numpy.array([[random.randint(1,100) for i in range(1,4)], [random.randint(1,100) for i in range(1,4)]])
c = numpy.concatenate((a, b))
d = numpy.concatenate((a, b), axis=0)
pprint(d)

a = numpy.array([
    [[random.randint(1,100) for i in range(1,4)], [random.randint(1,100) for i in range(1,4)], [random.randint(1,100) for i in range(1,4)]],
    [[6, 3, 8], [2, 3, 1], [4, 3, 3]],
    [[7, 8, 9], [9, 5, 6], [7, 4, 9]],
], float)
b = numpy.array([
    [[1, 2, 7], [4, 5, 9], [4, 5, 9]],
    [[6, 3, 8], [2, 3, 1], [4, 3, 3]],
    [[7, 8, 9], [9, 5, 6], [7, 4, 9]],
], float)
d = numpy.concatenate((a, b), axis=2)
pprint(d)