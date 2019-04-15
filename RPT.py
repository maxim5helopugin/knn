import numpy as np 
from queue import PriorityQueue
from random import gauss

class Tree:
	def __init__(self, S, n):
		self.c = 2
		self.m = 3
		self.n = n
		self.left = None
		self.right = None
		self.date = None

		if len(S)<=self.n:
			self.data = S
			return

		self.vectors = []
		for i in range(0,self.m):
			self.vectors.append(self.make_rand_vector(len(S[0])))

		ail = []
		air = []

		self.matrix_left = np.zeros((self.c,self.m))
		self.matrix_right = np.zeros((self.c,self.m))

		projections = []
		self.direction = self.make_rand_vector(len(S[0]))
		S = np.array(S)
		

		for point in S:
			projections.append(self.proj(point, self.direction))
		self.median = np.median(projections)

		rights = np.where(projections>=self.median)
		lefts = np.where(projections<self.median)

		## Does not actually get c closest points,
		## might need fix
		self.air = rights[0][0:self.c]
		self.ail = lefts[0][0:self.c]

		for i in range(0,self.c):
			for j in range(0,self.m):
				self.matrix_left[i][j] = np.dot(self.vectors[j],S[ail[i]])

		for i in range(0,self.c):
			for j in range(0,self.m):
				self.matrix_right[i][j] = np.dot(self.vectors[j],S[air[i]])

		self.left = Tree(S[lefts], self.n)
		self.right = Tree(S[rights], self.n)

	def make_rand_vector(self, dims):
	    vec = [gauss(0, 1) for i in range(dims)]
	    mag = sum(x**2 for x in vec) ** .5
	    return [x/mag for x in vec]

	def norm(self, v):
		return np.linalg.norm(v)

	def proj(self, u, v):
		return ((np.dot(u,v))/pow(self.norm(v),2))

	def print(self):
		print("in the root")
		if(self.left == None):
			print(self.data)
			return
		self.left.print()
		self.right.print()

	def guided_search(self, target, t):
		C_q = []
		B = binary_search_tree
		A = None
		ai = None
		P = PriorityQueue()
		new_vectors = []
		for vector in self.vectors:
			new_vectors.append(np.dot(vector,target))

		current_node = self

		if t > 0:
			while current_node.data == None:
				if np.dot(self.direction, target) < self.median:
					A = self.matrix_right
					ai = self.air
					current_node = self.right
				else:
					A = self.matrix_right
					ai = self.ail
					current_node = self.left
				########
				compute priority_value, set count = count+1
				Sort the rows of A in increasing order according to distance from new_vectors and let a have sorted indecies
				Insert {ai(a(1))...ai(a(c''))} into B with count
				struct = (count, current_node)
				P.insert(struct, priority_value)
			Leaf_q = indecies of S in leaf_node
			C_q = C_q union leaf_q 
			t = t - 1
			current_node = (P.extract_max).current_node
			P.extract_max.count delete from B
		return C_q union all candidates from B

				
#########################################################	
points = [[-1,1],[-1,3],[1,2],[2,1],[3,-1],[2,-3],[-2,-2]]
tree = Tree(points, 3)
tree.print()