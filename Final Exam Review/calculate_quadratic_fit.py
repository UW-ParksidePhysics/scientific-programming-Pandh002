import numpy as np
from numpy import polyfit

def calculate_quadratic_fit(data):
    """
    Read: quadratic polynomial coefficients, ordered constant term first, then linear term, and quadratic term last
    :param filename: quad
        Name of the file to be read
    :return: data: x-y data that is fit in a list
    """

    xvalues = data[0]
    yvalues = data[1]
    quadratic_coefficients = np.polyfit(xvalues, yvalues, 2)
    return quadratic_coefficients

if __name__ == '__main__':
    test_data = [np.linspace(-1,1), np.linspace(-1,1)**2]
    print(calculate_quadratic_fit(test_data))
