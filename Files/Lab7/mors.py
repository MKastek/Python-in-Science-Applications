# :=
import numpy as np

#refactoring
'''
m = np.random.random((100, 100))
x = m + 54
print(x)
'''

#x = (m := np.random.random((100, 100))) + 54
#print(m)

#lista macierzy

m = [np.random.random((100,100)) for _ in range(10)]
d = [det for matrix in m if (det := np.linalg.det(matrix)) > 0]
print(d)

