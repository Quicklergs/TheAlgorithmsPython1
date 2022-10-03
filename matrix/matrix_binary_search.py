def binary_search(array: list, lower_bound: int, upper_bound: int, value: int) -> bool:
    """
    This function carries out Binary search on a 1d array
    Array: A 1d sorted array
    lower_bound: the lowest index for the binary search algorithm
    upper_bound: the highest index for the binary search algorithm
    value : the value ment to be searched
    >>> matrix = [1, 4, 7, 11, 15]
    >>> target = 1
    >>> binary_search(matrix, 0, len(matrix) - 1, 1)
    True
    >>> target = 23
    >>> binary_search(matrix, 0, len(matrix) - 1, 1)
    False
    """
    r = int((lower_bound + upper_bound) // 2)
    if array[r] == value:
        return True
    if r in (lower_bound, upper_bound):
        return False
    if array[r] < value:
        return binary_search(array, r + 1, upper_bound, value)
    else:
        return binary_search(array, lower_bound, r, value)
def mat_bin_search(value: int, matrix: list) -> bool:
    """
    This function loops over a 2d matrix and calls binarySearch on the selected 1d array
    value : value ment to be searched
    matrix = a sorted 2d matrix
    >>> matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    >>> target = 1
    >>> mat_bin_search(target, matrix)
    True
    >>> target = 34
    >>> mat_bin_search(target, matrix)
    False
    """
    index = 0
    while matrix[index][0] < value:
        if binary_search(matrix[index], 0, len(matrix[index]) - 1, value):
            return True
        index += 1
    return False
