from pprint import pprint
import numpy


a = numpy.array([
    [[1, 2, 7], [4, 5, 9], [4, 5, 9]],
    [[6, 3, 8], [2, 3, 1], [4, 3, 3]],
    [[7, 8, 9], [9, 5, 6], [7, 4, 9]],
], float)
b = numpy.array([
    [[1, 2, 7], [9, 9, 9], [4, 5, 9]],
    [[6, 3, 8], [2, 3, 1], [4, 3, 3]],
    [[7, 8, 9], [9, 5, 6], [7, 4, 9]],
], float)
d = numpy.concatenate((a, b), axis=2)
pprint(d)