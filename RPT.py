# Maxim Shelopugin
#
# Random Projection Tree class

import numpy as np 
from random import gauss
from search import guided_search

# Tree class 
class Tree:
	def __init__(self, S, labels, n):
		self.c = 10
		self.m = 20
		self.n = n
		self.left = None
		self.right = None
		self.data = None
		self.isleaf = False
		self.labels = None

# If the size of the set is less than leaf size, return the leaf
		if len(S)<=self.n:
			self.data = S
			self.labels = labels
			self.isleaf = True
			return

# Get the random vectors
		self.vectors = []
		for i in range(0,self.m):
			self.vectors.append(self.make_rand_vector(len(S[0])))

# Generate matricies for the left and right partitions
		self.matrix_left = np.zeros((self.c,self.m))
		self.matrix_right = np.zeros((self.c,self.m))

# Generate the random projection
		projections = []
		self.direction = self.make_rand_vector(len(S[0]))

# convert data and labels to arrays
		S = np.array(S)
		labels = np.array(labels)
		
# Separate the points into different projections, get the median
		for point in S:
			projections.append(self.proj(point, self.direction))
		self.median = np.median(projections)

# Separate the points into two sub-trees
		rights = np.where(projections>=self.median)
		lefts = np.where(projections<self.median)

# Separate labels as well
		right_l = labels[rights]
		left_l = labels[lefts]

# Get the closest points to the median
		self.air = rights[0][0:self.c]
		self.ail = lefts[0][0:self.c]

		self.air_l = right_l[0:self.c]
		self.ail_l = left_l[0:self.c]

# Populate the guiding matricies
		for i in range(0,self.c):
			for j in range(0,self.m):
				self.matrix_left[i][j] = np.dot(self.vectors[j],S[self.ail[i]])

		for i in range(0,self.c):
			for j in range(0,self.m):
				self.matrix_right[i][j] = np.dot(self.vectors[j],S[self.air[i]])

# Set the matricies as datapoints rather than indecies
		self.air = S[self.air]
		self.ail = S[self.ail]

# Assign the left and right subtrees
		self.left = Tree(S[lefts], left_l, self.n)
		self.right = Tree(S[rights], right_l, self.n)

# Return the random vector with given dim
	def make_rand_vector(self, dims):
	    vec = [gauss(0, 1) for i in range(dims)]
	    mag = sum(x**2 for x in vec) ** .5
	    return [x/mag for x in vec]

# Return the norm of the vector
	def norm(self, v):
		return np.linalg.norm(v)

# Return the projection of u onto v
	def proj(self, u, v):
		return ((np.dot(u,v))/pow(self.norm(v),2))

# Test the tree
	def print(self):
		if(self.left == None and self.right == None):
			print(self.data)
			print(self.labels)
			return
		print("left")
		self.left.print()
		print("right")
		self.right.print()