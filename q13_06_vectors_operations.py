"""Q6. Vectors and Basic Operations."""

import numpy as np


v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

print("Vector 1:", v1)
print("Vector 2:", v2)

print("\nAddition:")
print(v1 + v2)

print("\nSubtraction:")
print(v1 - v2)

print("\nElement-wise Multiplication:")
print(v1 * v2)

print("\nDot Product:")
print(np.dot(v1, v2))
