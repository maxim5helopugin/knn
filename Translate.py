# Test Script for vanila KNN
# Linear Search
from Data_mnist import readmnist
from Data_svhn import readsvhn
from Data_heart import readheart
from Data_mice import readmice
import timeit

import numpy as np

# Calculate Euclidian distance between 2 vectors
def distance(x1, x2):
	return np.sqrt(np.sum(np.power((x1-x2),2)))

# Alias the countours of the dataset
def alias(dataset):
	for i in range(0, len(dataset)):
		for j in range(0, len(dataset[i])-1):
			dataset[i,j] += dataset[i, j+1]*0.1
	return dataset

# Distance calculation
def closest(x1, train):
	distances = np.zeros(train.shape[0])
	for i in range(0, distances.shape[0]):
		distances[i] = distance(x1, train[i])
	return np.argmin(distances)

# Return accuracy
def accuracy(correct, size):
	return correct/size;

# Run a test case
def run(testcase, do_alias = False):
	# Tests
	start = timeit.default_timer()
	if testcase=="mnist":
		data, labels, test_data, test_labels = readmnist()

	if testcase=="svhn":
		data, labels, test_data, test_labels = readsvhn()

	if testcase=="heart":
		data, labels, test_data, test_labels = readheart()

	if testcase=="mice":
		data, labels, test_data, test_labels = readmice()

	if do_alias:
		test_data = alias(test_data)

	correct = 0

	for i in range(0,len(test_data)):
		if i%100==0:
			print(i, end=" ")

		if labels[closest(test_data[i], data)] == test_labels[i]:
			correct+=1

	print()
	print(accuracy(correct, len(test_data)))
	print("--------------")
	stop = timeit.default_timer()
	print("took ", stop-start, "seconds")
	print("--------------\n")

#run("mnist")
#run("mnist", True)
#run("svhn")
#run("svhn", True)
run("heart")
run("heart", True)
run("mice")
run("mice", True)