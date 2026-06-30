"""Q1. Basic Array Creation."""

import numpy as np


one_d_array = np.array([10, 20, 30, 40, 50])
two_d_array = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
)

print("1D Array:")
print(one_d_array)
print("Shape:", one_d_array.shape)
print("Data Type:", one_d_array.dtype)

print("\n2D Array:")
print(two_d_array)
print("Shape:", two_d_array.shape)
print("Data Type:", two_d_array.dtype)
