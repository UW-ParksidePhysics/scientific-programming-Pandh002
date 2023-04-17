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
    final_temperature = 0.5 * mass_ratio * initial_speed ** 2 + initial_temperature
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
    if input_units == 'mph' and output_units == 'm/s':
        output_value = input_value * miles_to_meters/hours_to_seconds
    elif input_units == 'lbs' and output_units == 'kg':
        output_value = input_value * pounds_to_kilograms
    return output_value


if __name__  == "__main__":
    print("calculating tire heat")

    tire_data_url = 'https://www.justtires.com/en-US/learn/load-index-speed-rating'
    ratings, load_indexes = extract_tire_data(tire_data_url)
    tire_speed_ratings = ratings['Maximum speed (MPH)'][0:7].astype('float').to_numpy()

    test_mass = 1
    print(f"{convert_units(test_mass, 'lbs', 'kg')}")

   # https://www.matweb.com/search/datasheet_print.aspx?matguid=6588439546ac4492965c894ddff3f5da
    tire_specific_heat = 0.440  ## J/g°C

comment- convert lbs to kg

