import numpy as np


def fit_curve_array(quadratic_coefficients, xmin, xmax, number_of_points=100):
    xvals = np.linspace(xmin, xmax, number_of_points)
    yvals = np.polynomial.polynomial.polyval(xvals, quadratic_coefficients)
    fit_curve = np.array((xvals, yvals))
    """read fit curve array
       :param filename: fit curve
           name of the file to read
           :return data: ndarray shape
               fit xy data to form function
       """
    return fit_curve


if __name__ == '__main__':
    quadratic_coefficients = [0, 0, 1]
    print(fit_curve_array(quadratic_coefficients, -2, 2))
