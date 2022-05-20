import math
import numpy as np


# normalize an given vector
from numpy import save


def make_vector_normal(x, y, z):
    vector_absolute_value = math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
    return_value = [x / vector_absolute_value, y / vector_absolute_value, z / vector_absolute_value]
    return return_value

#create idealvector in direction of light
def create_perfect_vector(vector_width, vector_height):
    sample_width = 40
    sample_hight = 40
    base_vector = np.ndarray(shape=(vector_width, vector_height, 8, 3), dtype=float, order='F')
    #light_array= calculate_light_position(30,30)
    light_array= calculate_light_direction_vector(39,70)
    for i in range(vector_width):
        for j in range(vector_height):
            for k in range(8):

                x_cordinate = (i - vector_width/2) * sample_width / vector_width
                y_cordinate = (i - sample_hight/2) * sample_hight / vector_height

                dX = light_array[k, 0] - x_cordinate
                dY = light_array[k, 1] - y_cordinate
                dZ = light_array[k, 2]

                base_vector[i, j, k, :] = make_vector_normal(dX, dY, dZ)

    save('data.npy', base_vector)
    print(base_vector[0, 949, 4, ...])
    print(base_vector[949, 0, 4, ...])


# calculate coordinate of lights in kartesisches system based distance from center and angle
def calculate_light_direction_vector(angle, r):
    light_array = np.ndarray(shape=(8, 3), dtype=float, order='F')
    for i in range(8):
        light_array[i, 0] = round(r * math.sin(math.radians(angle)) * math.cos(math.radians(-90 + (i * 45))), 5)
        light_array[i, 1] = round(r * math.sin(math.radians(angle)) * math.sin(math.radians(-90 + (i * 45))), 5)
        light_array[i, 2] = round(r * math.cos(math.radians(angle)), 5)
       # print(light_array[i, :])
    return light_array

def calculate_light_position(radius, height):
    distance = math.sqrt(radius ** 2 + height ** 2)
    angle = math.acos(height / distance)
    light_array = calculate_light_direction_vector(math.degrees(angle), distance)
    return light_array
