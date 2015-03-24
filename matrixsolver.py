import numpy

a = ([1, 0, 0]
	,[0, 1, 0]
	,[0, 0, 1])
b = ([1, 1, 1])
x = numpy.linalg.solve(a, b)
print x
