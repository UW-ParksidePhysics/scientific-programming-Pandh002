"""
read in calculate quadratic fit
"""

__author__ = 'Trevor Pandher'

import numpy as np

def calculate_quadratic_fit(filename):
    """
    read in two columns of data from text file of arbitrary length
    :param filename:
        Name of the file
    :return data: 
        columns of the data as rows of array
    """
    try:
        data = np.loadtxt(filename).transpose()
        return data
    except OSError as error:
        print(f'{error}')


if __name__ == "__main__":
    test_file = 'volumes_energies.dat'
    test_data = read_two_columns_text(test_file)
    print(f'test_data = {test_data=}, shapes = {test_data.shape}')

