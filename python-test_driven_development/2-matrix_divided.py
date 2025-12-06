#!/usr/bin/python3
"""
Module 2-matrix_divided
Provides a function that divides all elements of a matrix by `div`.

- The matrix must be a list of equal-length lists of ints/floats.
- `div` must be an int/float (bools are not accepted).
- Division by zero raises ZeroDivisionError.
- Returns a NEW matrix with values rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by `div`, rounded to 2 dp."""
    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_msg = "Each row of the matrix must have the same size"

    # Validate matrix structure
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(type_msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(type_msg)
    if any(len(row) == 0 for row in matrix):
        raise TypeError(type_msg)

    # Validate matrix elements (no bools)
    for row in matrix:
        for val in row:
            if not isinstance(val, (int, float)) or isinstance(val, bool):
                raise TypeError(type_msg)

    # Validate row lengths
    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError(size_msg)

    # Validate div (no bools)
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element, round to 2 decimals, and normalize -0.0 to 0.0
    result = []
    for row in matrix:
        new_row = []
        for val in row:
            q = round(val / div, 2)
            if q == 0:  # catches 0.0 and -0.0
                q = 0.0
            new_row.append(q)
        result.append(new_row)
    return result
