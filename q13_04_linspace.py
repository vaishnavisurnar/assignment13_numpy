"""Q4. np.linspace()."""

import numpy as np


numbers_between_0_and_5 = np.linspace(0, 5, 10)
numbers_between_minus_10_and_10 = np.linspace(-10, 10, 15)

print("10 Equally Spaced Numbers Between 0 and 5:")
print(numbers_between_0_and_5)
print("Length:", len(numbers_between_0_and_5))

print("\n15 Equally Spaced Numbers Between -10 and 10:")
print(numbers_between_minus_10_and_10)
print("Length:", len(numbers_between_minus_10_and_10))
