modules = ['read_two_columns', 'calculate_bivariate_statistics', 'calculate_quadratic_fit', 'fit_curve_array', 'plot_data_with_fit', 'calculate_lowest_eigenvectors']
for module in modules:
    with open(module+'.py') as module_file:
        exec(module_file.read())
