
"""
read plot data with fit from fit curve array
"""

__author__ = 'Trevor Pandher'

import numpy as np

def read_two_columns_text(filename):
    """
    read plot data with fit from text file of fit curve array
    :param filename: ndarray, shape (2, M)
    x-y data that was fit. M is the number of data points
        Name of the file to be read
    :return data: ndarray
        columns of the data as rows of array
    """