import random
from numpy import genfromtxt
import numpy as np

# read the mice dataset and return the necessary data
def readmice():
	my_data = genfromtxt('Bio/mice.csv', delimiter=',')
	my_data = my_data[1:]

	my_data = np.nan_to_num(my_data)

	np.random.seed(11)
	my_data = np.random.permutation(my_data)
	return my_data[:250, :-1], my_data[:250, -1], my_data[250:,:-1], my_data[250:,-1]
