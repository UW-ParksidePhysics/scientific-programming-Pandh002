import numpy as np
import matplotlib.pyplot as plt


def calculate_final_temperature(masses, specific_heat, initial_speed, initial_temperature):
    """
    calculates the final temperature by equating the kinetic energy change to heat flow
    :param masses: list [heat sink mass, kinetic mass]
    :param specific_heat:
    :param initial_speed:
    :param initial_temperature:
    :return:  final_temperature
    """
    mass_ratio = sum(masses) / masses[0]
    final_temperature = 0.5 * (mass_ratio/specific_heat) * initial_speed ** 2 + initial_temperature
    return final_temperature


def extract_tire_data(url):
    """

    :param url:
    :return: speed ratings, tire load indexes
    """
    import pandas as pd
    url_tables=pd.read_html(url)
    speed_ratings=url_tables[0]
    tire_load_indexes=url_tables[1]
    return speed_ratings, tire_load_indexes

def convert_units(input_value, input_units, output_units):
    """

    :param input_value:
    :param input_units:
    :param output_units:
    :return: output value in output units
    """
    miles_to_meters = 1609.344
    hours_to_seconds = 3600
    pounds_to_kilograms = 0.45359237
    grams_to_kilograms = 1e-3
    if input_units == 'mph' and output_units == 'm/s':
        output_value = input_value * miles_to_meters/hours_to_seconds
    elif input_units == 'lbs' and output_units == 'kg':
        output_value = input_value * pounds_to_kilograms
    elif input_units == "J/g°C" and output_units == 'J/kg K':
        output_value = input_value / grams_to_kilograms
    return output_value


if __name__  == "__main__":
    print("calculating tire heat")

    tire_data_url = 'https://www.justtires.com/en-US/learn/load-index-speed-rating'
    ratings, load_indexes = extract_tire_data(tire_data_url)
    tire_speed_ratings = ratings['Maximum speed (MPH)'][0:7].astype('float').to_numpy()
    tire_load = load_indexes['Load (lbs)'].astype('float').to_numpy()

    tire_speed_ratings = convert_units(tire_speed_ratings, 'mph', 'm/s')
    tire_load = convert_units(tire_load, 'lbs', 'kg')

    print(f'v = {tire_speed_ratings[-1]}')

  # https://www.matweb.com/search/datasheet_print.aspx?matguid=6588439546ac4492965c894ddff3f5da
    tire_specific_heat = 0.440  ## J/g°C
    tire_specific_heat = convert_units(tire_specific_heat, "J/g°C", "J/kg K")
    print(f'c = {tire_specific_heat}')
    tire_mass = convert_units(18, 'lbs', 'kg')
    print(f'm_l = {tire_load[-1]}')
    print(f'm_T = {4*tire_mass}')
    print(f'm_k/m_T = {(tire_load[-1]+4*tire_mass)/(4*tire_mass)}')
    print(f'm_k/m_T/c = {(tire_load[-1] + 4 * tire_mass) / (4 * tire_mass*tire_specific_heat)}')
    print(f'v^2 = {tire_speed_ratings[-1]**2}')
    print(f'0.5 m_k/m_T/c v^2 = {0.5*(tire_load[-1] + 4 * tire_mass)*tire_speed_ratings[-1]**2 / (4 * tire_mass*tire_specific_heat)}')


    starting_temperature = 273.15 + 25
    for load in tire_load:
        total_mass = 4 * tire_mass + load
        #print(total_mass)
        temperatures = calculate_final_temperature([4*tire_mass, total_mass], tire_specific_heat, tire_speed_ratings,
                                                   starting_temperature)

        plt.plot(tire_speed_ratings, temperatures-starting_temperature, label=f'{load:.0f}')
# label the x-axis using xlabel, label y-axis using ylabel, create a legend using
    #labelequals in play command plt.function
    plt.xlabel("Velocity at the start of the skid [m/s]")
    plt.ylabel("Temperature change of tire [K]")

    plt.legend(title="Load (kg)", ncols=2)
    plt.show()


