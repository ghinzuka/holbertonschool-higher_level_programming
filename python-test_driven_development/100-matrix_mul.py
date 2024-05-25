#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
            m_a (list): The first matrix represented as a list of lists.
            m_b (list): The second matrix represented as a list of lists.

    Returns:
            list: The resulting matrix after multiplying m_a and m_b.

    Raises:
            TypeError: If m_a or m_b is not a list or if m_a
or m_b is not a list of lists.
            ValueError: If m_a or m_b is empty or
if the dimensions of m_a and m_b are not compatible.
            TypeError: If m_a or m_b contains elementements
that are not integers or floats.

    """
    # Check if m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # Check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_size_a = None
    for row in m_a:
        if row_size_a is None:
            row_size_a = len(row)
        elif len(row) != row_size_a:
            raise TypeError("each row of m_a must be of the same size")
    row_size_b = None
    for row in m_b:
        if row_size_b is None:
            row_size_b = len(row)
        elif len(row) != row_size_b:
            raise TypeError("each row of m_b must be of the same size")

    if row_size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            celementl_sum = 0
            for k in range(row_size_a):
                celementl_sum += m_a[i][k] * m_b[k][j]
            result_row.append(celementl_sum)
        result.append(result_row)

    return result
