# Maxim Shelopugin
#
# Script that runs all the datasets on vanila knn, aliased knn and tree knn

from Data_mnist import readmnist
from Data_svhn import readsvhn
from Data_heart import readheart
from Data_mice import readmice
import timeit
from RPT import Tree
from search import guided_search

import numpy as np

# Calculate Euclidian distance between 2 vectors
def distance(x1, x2):
	return np.sqrt(np.sum(np.power((x1-x2),2)))

# Alias the countours of the dataset
def alias(dataset):
	for i in range(0, len(dataset)):
		for j in range(0, len(dataset[i])- 1):
			if dataset[i, j] == 0:
				dataset[i, j] = dataset[i, j+1]/2;
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
def run(testcase, do_alias = False, tree = False):
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

	print(testcase)

	if tree:
		subset = Tree(data, labels,  100)
		vectors = []
		for i in range(0,subset.m):
			vectors.append(subset.make_rand_vector(len(data[0])))

	for i in range(0,len(test_data)):

		if tree:
			data, labels = guided_search(subset, test_data[i], 3, vectors)
			data = np.array(data)
			labels = np.array(labels)

		if labels[closest(test_data[i], data)] == test_labels[i]:
			correct+=1

	print(accuracy(correct, len(test_data)))
	stop = timeit.default_timer()
	print("took ", stop-start, "seconds")
	print("--------------\n")

run("heart")
run("heart", True)
run("heart", tree=True)
run("heart", True, tree = True)

run("mice")
run("mice", True)
run("mice", tree = True)
run("mice", True, tree = True)

run("mnist")
run("mnist", True)
run("mnist", tree = True)
run("mnist", True, tree = True)

run("svhn")
run("svhn", True)
run("svhn", tree = True)
run("svhn", True, tree = True)