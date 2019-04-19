import random
from numpy import genfromtxt
import numpy as np

# read the heart attack dataset and return the necessary data
def readheart():
	my_data = genfromtxt('Bio/heart.csv', delimiter=',', dtype = 'int32')
	my_data = my_data[1:]

	np.random.seed(11)
	my_data = np.random.permutation(my_data)
	return my_data[:250, :-1], my_data[:250, -1], my_data[250:,:-1], my_data[250:,-1]