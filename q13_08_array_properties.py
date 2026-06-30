"""Q8. Properties of Arrays."""

import numpy as np


np.random.seed(13)

matrix = np.random.randint(1, 101, size=(4, 4))

print("4x4 Matrix of Random Integers:")
print(matrix)
print("\nShape:", matrix.shape)
print("Dimension:", matrix.ndim)
print("Total Number of Elements:", matrix.size)
print("Data Type:", matrix.dtype)
print("Minimum Value:", matrix.min())
print("Maximum Value:", matrix.max())
