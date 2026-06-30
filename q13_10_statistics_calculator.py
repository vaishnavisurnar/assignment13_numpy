"""Q10. Mini Project - Simple Statistics Calculator using NumPy."""

import numpy as np


def print_row_wise_sum(numbers):
    """Reshape the array into a useful 2D form and print row-wise sums."""
    possible_columns = [5, 4, 3, 2]

    for columns in possible_columns:
        if numbers.size % columns == 0 and numbers.size != columns:
            matrix = numbers.reshape(-1, columns)
            print(f"\nReshaped 2D Array ({matrix.shape[0]} x {matrix.shape[1]}):")
            print(matrix)
            print("Row-wise Sum:")
            print(matrix.sum(axis=1))
            return

    print("\nReshape into a proper 2D array is not possible for this size.")


def main():
    """Generate random numbers and calculate basic statistics."""
    try:
        count = int(input("How many numbers do you want to generate? "))

        if count <= 0:
            print("Please enter a positive number.")
            return

        np.random.seed(13)
        numbers = np.random.randint(10, 101, size=count)

        print("\nGenerated Array:")
        print(numbers)
        print("\nMean:", np.mean(numbers))
        print("Median:", np.median(numbers))
        print("Standard Deviation:", np.std(numbers))
        print("Minimum:", np.min(numbers))
        print("Maximum:", np.max(numbers))

        print_row_wise_sum(numbers)

    except ValueError:
        print("Invalid input. Please enter an integer value.")


main()
