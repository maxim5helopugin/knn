import numpy as np 
from random import gauss
from search import guided_search

# Random Projection Tree
class Tree:
	def __init__(self, S, n):
		self.c = 2
		self.m = 3
		self.n = n
		self.left = None
		self.right = None
		self.data = None
		self.isleaf = False

# If the size of the set is less than leaf size, return the leaf
		if len(S)<=self.n:
			self.data = S
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
		S = np.array(S)
		
# Separate the points into different projections, get the median
		for point in S:
			projections.append(self.proj(point, self.direction))
		self.median = np.median(projections)

# Separate the points into two sub-trees
		rights = np.where(projections>=self.median)
		lefts = np.where(projections<self.median)

		## Does not actually get c closest points,
		## might need fix
# Get the closest points to the median
		self.air = rights[0][0:self.c]
		self.ail = lefts[0][0:self.c]

# Populate the guiding matricies
		for i in range(0,self.c):
			for j in range(0,self.m):
				self.matrix_left[i][j] = np.dot(self.vectors[j],S[self.ail[i]])

		for i in range(0,self.c):
			for j in range(0,self.m):
				self.matrix_right[i][j] = np.dot(self.vectors[j],S[self.air[i]])

# Assign the left and right subtrees
		self.left = Tree(S[lefts], self.n)
		self.right = Tree(S[rights], self.n)

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
			return
		print("left")
		self.left.print()
		print("right")
		self.right.print()
				
#########################################################	
points = [[-1,1],[-1,3],[1,2],[2,1],[3,-1],[2,-3],[-2,-2]]
tree = Tree(points, 3)
tree.print()

vectors = []
for i in range(0,tree.m):
	vectors.append(tree.make_rand_vector(len(points[0])))

guided_search(tree, [-1,1], 1, vectors)