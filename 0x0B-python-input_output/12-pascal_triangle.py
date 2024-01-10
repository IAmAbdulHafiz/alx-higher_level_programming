#!/usr/bin/python3

"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    my_triangles = [[1]]
    while len(my_triangles) != n:
        my_triangle = my_triangles[-1]
        tmp = [1]
        for i in range(len(my_triangle) - 1):
            tmp.append(my_triangle[i] + my_triangle[i + 1])
        tmp.append(1)
        my_triangles.append(tmp)
    return my_triangles
