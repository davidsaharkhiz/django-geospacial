import os
import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
print("test")

print(a.shape)

print(a.ndim)
print(a.dtype.name)
print(a.itemsize)

print("creating 24 elements nad putting in a 3d-array")
c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)

print(a.size)
