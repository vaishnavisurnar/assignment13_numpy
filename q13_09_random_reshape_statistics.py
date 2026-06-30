"""Q9. Combined - Random + Reshape + Statistics."""

import numpy as np


np.random.seed(13)

array_1d = np.random.randint(1, 51, size=20)
matrix = array_1d.reshape(4, 5)

print("Original 1D Array:")
print(array_1d)

print("\nReshaped 4x5 Matrix:")
print(matrix)

print("\nSum:", matrix.sum())
print("Mean:", matrix.mean())
print("Standard Deviation:", matrix.std())
print("Maximum Value in Each Row:")
print(matrix.max(axis=1))
