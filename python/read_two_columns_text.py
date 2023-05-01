"""
read in two columns of data from text file of arbitrary length
"""

__author__ = 'Trevor Pandher'


import numpy as np

def read_two_columns_text(filename):
    """
    read in two columns of data from text file of arbitrary length
    :param filename: str
        Name of the file to be read
    :return data: ndarray
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
