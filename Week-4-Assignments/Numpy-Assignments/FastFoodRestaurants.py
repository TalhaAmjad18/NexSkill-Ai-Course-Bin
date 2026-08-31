import numpy as np

lat, long, pos = np.genfromtxt('Week 4 Assignments\Numpy Assignments\FastFoodRestaurants.csv', delimiter=',', usecols=(4,5,7), skip_header=True, dtype=None, unpack=True)