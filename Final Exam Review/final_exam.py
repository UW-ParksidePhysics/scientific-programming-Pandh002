import matplotlib.pyplot as plt
import numpy as np

from datetime import date
from read_two_columns import two_columns
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from convert_units import convert_units
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from annotate_plot import annotate_plot
from equations_of_state import *


if __name__ == "__main__":
    filename = 'Si.Fd-3m.GGA-PBE.volumes_energies.dat'


    def parse_file_name():
        filename_split = filename.split(".")[0:3]
        chemical_symbol = filename_split[0]
        crystal_symbol = filename_split[1]
        density_correlation = filename_split[2]
        return chemical_symbol, crystal_symbol, density_correlation



    read_two_columns_data = (read_two_columns_text(filename)) / 2
    statistical_data = calculate_bivariate_statistics(two_columns_data)
    quad_fit_data = calculate_quadratic_fit(two_columns_data)

    fit_eos_curve, fit_eos_parameters = fit_eos(two_columns_data[0], two_columns_data[1],
                                                quad_fit_data, eos='birch-murnaghan')
    x_fit_curve = fit_curve_array(quad_fit_data, statistical_data[2], statistical_data[3], number_of_points=50)

    volume_list1 = convert_units(x_fit_curve[0], 'bohr/atom', 'angstrom**3/atom')
    energy_list1 = convert_units(x_fit_curve[1], 'rydberg/atom', 'eV/atom')
    bulk_modulus = convert_units(fit_eos_parameters[1], 'rydberg/bohr**3', 'gigapascals')

    volume_list2 = [convert_units(two_column_data[0], 'bohr/atom', 'angstrom**3/atom')]
    energy_list2 = [convert_units(two_column_data[1], 'rydberg/atom', 'eV/atom')]

    plt.plot(volume_list1, energy_list1, color='black')
    plt.plot(volume_list2, energy_list2, 'bo')

    plt.xlim(x_limits[0], x_limits[1])
    plt.ylim(y_limits[0], y_limits[1])
    plt.xlabel(r'$V\/(\mathrm{Å^3/atom})$')
    plt.ylabel(r'$E\/(\mathrm{eV/atom})$')

    x_range = np.max(volume_list1) - np.min(volume_list1)
    y_range = np.max(energy_list1) - np.min(energy_list1)
    x_limits = [np.min(volume_list1) - (0.1 * x_range), np.max(volume_list1) + (0.1 * x_range)]
    y_limits = [np.min(energy_list1) - (0.1 * y_range), np.max(energy_list1) + (0.1 * y_range)]

    annotate_plot({'string': f"Created by 'Trevor' \n {date.today().isoformat()}",
                   'position': np.array([np.min(volume_list1), np.min(energy_list1)]), 'alignment': ['left', 'bottom'], 'fontsize': 10})
    plt.show()
  
