import numpy as np
from scipy import stats


def calculate_bivariate_statistics(filename):
    """
    Read: mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value; maximum y-value
        :return data: ndarray
            list of data as array
    """
    if len(filename) != 2 or len(filename[0]) <= 1:
        raise IndexError

    stat = stats.describe(filename, axis=1)
    mean_of_y = stat[2][1]
    standard_deviation_of_y = np.sqrt(stat[3][1])

    min_xval = stat.minmax[0][0]
    min_yval = stat.minmax[0][1]
    max_xval = stat.minmax[1][0]
    max_yval = stat.minmax[1][1]
    statistics = [mean_of_y, standard_deviation_of_y, min_xval, min_yval, max_xval, max_yval]

    return statistics


if __name__ == "__main__":
    xvalues = np.linspace(-10, 10, 21)
    yvalues = xvalues ** 2
    test_data = np.array([xvalues, yvalues])
    print(calculate_bivariate_statistics(test_data))
