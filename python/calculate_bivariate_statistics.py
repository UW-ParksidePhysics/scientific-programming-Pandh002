"""
read in two columns of data from text file of arbitrary length
"""

__author__ = 'Trevor Pandher'


import numpy as np

def calculate_bivariate_statistics(filename):
    """
    read in two columns of data from text file of arbitrary length
    :param data: ndarray, shape(2, M)
 x-y data to be characterized. M is the number of data points.
    :return statistics: ndarray, shape (6,)
Mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value
    """
#Make fit curve using fit polynomial coefficients, NumPy's polynomialLinks to an external site., and minimum and maximum x-values
