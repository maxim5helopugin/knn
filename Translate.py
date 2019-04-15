from Data_mnist import readmnist
from Data_svhn import readsvhn
import numpy as np

def distance(x1, x2):
	return np.sqrt(np.sum(np.power((x1-x2),2)))

def closest(x1, train):
	distances = np.zeros(train.shape[0])
	for i in range(0, train.shape[0]):
		distances = distance(x1, train[i])
	return np.argmin(distances)

data, labels, test_data, test_labels = readmnist()
print(labels[closest(test_data[0], data)]) 
