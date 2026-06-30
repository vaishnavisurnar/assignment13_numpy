"""Q5. Random Arrays."""

import numpy as np


np.random.seed(13)

random_1d = np.random.rand(10)
random_normal_matrix = np.random.randn(3, 3)
random_integer_matrix = np.random.randint(10, 51, size=(4, 5))

print("1D Array of 10 Random Numbers Between 0 and 1:")
print(random_1d)

print("\n3x3 Matrix from Standard Normal Distribution:")
print(random_normal_matrix)

print("\n4x5 Array of Random Integers Between 10 and 50:")
print(random_integer_matrix)
