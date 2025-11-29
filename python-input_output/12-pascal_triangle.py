#!/usr/bin/python3
"""
This module defines a function that generates Pascal's Triangle.
It demonstrates list manipulation and combinatorial logic.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal triangle of n.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists containing the triangle integers.
              Returns an empty list if n <= 0.
    """
    # Handle edge case: non-positive integers return empty list
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Loop to generate subsequent rows (starting from row 1 to n-1)
    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]  # Every row starts with 1

        # Calculate the middle numbers
        # We sum the two numbers "above" (index j and j+1 of previous row)
        for j in range(len(prev_row) - 1):
            current_row.append(prev_row[j] + prev_row[j + 1])

        current_row.append(1)  # Every row ends with 1
        triangle.append(current_row)

    return triangle
