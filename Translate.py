# Test Script for vanila KNN
# Linear Search
from Data_mnist import readmnist
from Data_svhn import readsvhn
import numpy as np

# Calculate Euclidian distance between 2 vectors
def distance(x1, x2):
	return np.sqrt(np.sum(np.power((x1-x2),2)))

# SVHN distance calculation
def closest_svhn(x1, train):
	distances = np.zeros(train.shape[-1])
	for i in range(0, distances.shape[0]):
		distances[i] = distance(x1, train[:,:,i])
	return np.argmin(distances)

# Mnist distance calculation
def closest_mnist(x1, train):
	distances = np.zeros(train.shape[0])
	for i in range(0, distances.shape[0]):
		distances[i] = distance(x1, train[i])
	return np.argmin(distances)
	
# Tests
data, labels, test_data, test_labels = readmnist()
for i in range(0,10):
	print(labels[closest_mnist(test_data[i], data)]) 
	print(test_labels[i])
	print("--------")

data, labels, test_data, test_labels = readsvhn()
for i in range(0,10):
	print(labels[closest_svhn(test_data[:,:,i], data)]) 
	print(test_labels[i])
	print("--------")