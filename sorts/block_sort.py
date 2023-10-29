def block_sort(lst: list) -> list:
    """
    Sorts a list using the Block Sort algorithm.

    The Block Sort algorithm works by dividing the input list into blocks of size
    sqrt(n), sorting each block, and then merging the sorted blocks into a single
    sorted list.

    Args:
        lst (List[int]): The unsorted list to be sorted.

    Returns:
        List[int]: The sorted list.

    Examples:
        >>> block_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        >>> block_sort([5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5]
        >>> block_sort([])
        []
        >>> block_sort([1, 1, 1, 1, 1])
        [1, 1, 1, 1, 1]
        >>> block_sort([7, 6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6, 7]
        >>> block_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        >>> block_sort([1])
        [1]
        >>> block_sort([2, 1])
        [1, 2]
        >>> block_sort([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        >>> block_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> block_sort([1000, 100, 10, 1, 10000, 100000, 1000000])
        [1, 10, 100, 1000, 10000, 100000, 1000000]
    """
    if not lst:
        return []

    block_size = int(len(lst) ** 0.5)
    blocks = [lst[i : i + block_size] for i in range(0, len(lst), block_size)]
    for block in blocks:
        block.sort()

    sorted_result = []  # Initialize an empty list to store the sorted elements.

    # Continue the loop until all blocks are merged.
    while blocks:
        # Find the block with the minimum first element.
        min_block = min(blocks, key=lambda block: block[0])

        # Append the minimum element to the sorted result.
        sorted_result.append(min_block.pop(0))

        # If the block is empty after the pop operation,
        # remove it from the list of blocks.
        if not min_block:
            blocks.remove(min_block)

    return sorted_result


if __name__ == "__main__":
    import doctest

    doctest.testmod()