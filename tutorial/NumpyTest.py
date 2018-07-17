import numpy

world_alcohol = numpy.genfromtxt("world_alcohol.txt", delimiter=",", dtype=str)
print(type(world_alcohol))
# print(world_alcohol)

vector = numpy.array([5, 10, 15, 20])
matrix = numpy.array([[5, 10, 15],
                      [20, 25, 30],
                      [30, 35, 40]])
print(vector.dtype)
print(matrix)
