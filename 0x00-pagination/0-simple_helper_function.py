#!/usr/bin/env python3

'''
Module to return the start index of desired page items within
a dataset
'''


def index_range(page: int, page_size: int) -> tuple[int, int]:
    '''
    Returns the start index and end_index based on th
    page and page_size of a given dataset

    Args:
        Page (int): Page to be accessed
        Page_size (int): Size of each page within a dataset

    Returns:
        Tuple: Containig start_index and end index of a page

    Examples:
        >>> index_range(3, 10)
        (20, 30)

        >>> type(index_range(3, 10))
        <class 'tuple'>

        >>> index_range(1, 7)
        (0, 7)

        >>> index_range(3, 15)
        (30, 45)
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + (page_size)

    return start_index, end_index
