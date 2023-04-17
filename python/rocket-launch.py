import matplotlib.pyplot as plt
import numpy as np

"""
This will contain the equations needed for my three plots:
position v time
velocity v time
acceleration v time
mass v time (data allowing)
"""

# some constants (will eventually be moved to a text file)
# Saturn V
mass_saturn = 2800000  # kg
thrust_saturn = 34500000  # N
# Falcon 9
mass_falcon = 540054  # kg
thrust_falcon = 7607000  # N
# SLS Block 1
mass_block = 26082156  # kg
thrust_block = 3991613  # N  !!! fact check this !!!

time_range = np.arange(0, 601, 0.1)


def total_mass():
    rocket_mass_array = [mass_saturn, mass_falcon, mass_block]
    payload = 8300  # kg, the largest payload possible that can be used by all three rockets
    collective_mass = payload + rocket_mass_array[0]
    return collective_mass


def saturn_rocket_simulation(collective_mass):
    thrust_array = [thrust_saturn, thrust_falcon, thrust_block]
    time = 0
    dm = 0.1  # change in mass
    gravity = 9.81  # m/s/s
    initial_velocity = 0
    position_array = []
    velocity_array = []
    acceleration_array = []
    for t in time_range:
        position = initial_velocity * (time+t) + (1 / 2) * \
                   ((thrust_array[0] - gravity) / (collective_mass - dm)) * (time+t) ** 2
        velocity = (thrust_array[0] - gravity) / (collective_mass - dm) * (time+t)
        acceleration = (thrust_array[0] - (collective_mass - dm) * gravity) / (collective_mass - dm)
        position_array.append(position)
        velocity_array.append(velocity)
        acceleration_array.append(acceleration)
        collective_mass = collective_mass - dm
    return position_array, velocity_array, acceleration_array
   # position = initial_velocity * time + (1 / 2) * ((thrust_array[i] - gravity) / (collective_mass - dm)) * time ** 2
   # velocity = (thrust_array[i] - gravity) / (collective_mass - dm) * time
   # acceleration = (thrust_array[i] - (collective_mass - dm) * gravity) / (collective_mass - dm)
    #position_array.append(position)
    #velocity_array.append(velocity)
    #acceleration_array.append(acceleration)
    #time = time + dt
   # collective_mass = collective_mass - dm
   # return position_array, velocity_array, acceleration_array


# print(saturn_rocket_simulation(total_mass())[0])
#print(saturn_rocket_simulation(total_mass())[1])
# print(saturn_rocket_simulation(total_mass())[2])


# position plot
plt.plot(time_range, saturn_rocket_simulation(total_mass())[0])
plt.show()

# velocity plot
plt.plot(time_range, saturn_rocket_simulation(total_mass())[1])
plt.show()

# acceleration plot
plt.plot(time_range, saturn_rocket_simulation(total_mass())[2])
plt.show()


# # Draft code comments
#
# Does the code run without error?
## yes, it ran without error
# If any error occurs, can you suggest a potential fix?
## N/A
# How understandable is the output of the code?
## To find the force in Newtons from its displacement
# Point out any parts you do not understand.
## On line 28 why did they put kg in the comment instead of the code itself
# How readable is the code itself?
## There are comments spread throughput to inform us what they were trying to conclude.
# Say where formatting or commenting would make the code more readable or where PEP-8 is violated.
## Commenting was used often, it helps the reader to understand why the number seen is there.
# How clearly do the code comments describe the problem it is trying to solve?
## The code comments are really well thought out.
# Identify places that would benefit from a clearer comment.
## Line 21, could use a clearer comment because it states that the thrust block should be double checked, they could say (has been checked)
# How clearly do the variable names relate to the concepts they concretize?
## Variable names are well thought out and are not similar to other names in its catagory
# Point out any variables you don't recognize, and/or suggest better names. Check for PEP-8 compliance.
## They used thrust, collective, and mass for the three different rockets. It is pretty simple naming
# How well does the range of variables capture the problem described?
## The objects are so large... being planets and rockets that the range of variables are fairly similar
# Identify extraneous regions that could be left out or important regions that should be included.
## The code is small and only uses 51 lines, keeping it simple helps to keep track of information
# To what degree does the script follow a functional programming paradigm, packaging all major components of the script
# into separately defined functions that pass information among them in a small number of lines? Identify ways in which
# the functionalization of the code could be improved.
## The plots from the code seem kinda basic, although it is a rough version, it will look better in the future
# How clearly do the visualizations show the solutions to the problem?
## There are three seperate graphs that are produced. if graphs were to be titled and labeled, it may be easier to read
# Say if there is extraneous whitespace or the co-domain or domain of the data should be changed or any other ways the
# visualizations could be more effective
## The scale for the images seems to be ok as the line ends at both ends of the page. the only thing I would
##  add would be titles and x/ylabels
