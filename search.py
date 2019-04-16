from queue import PriorityQueue
import numpy as np

def priority(U, v, q):
	return 1 / np.linalg.norm(v - np.dot(U,q))

def distance(x, q):
	return np.linalg.norm(x-q)

def guided_search(root, q, t, vectors):
	#C_q = []
	B = [] # needs to be bst
	A = None
	ai = None
		
	P = PriorityQueue()
	count = 0
	q_not = []
# Get independent random vectors, create a set q_not
	for vector in vectors:
		q_not.append(np.dot(vector,q))

# Current node = root 
	current_node = root

	if t > 0:
		while not current_node.isleaf:
			if np.dot(current_node.direction, q) < current_node.median:
				A = current_node.matrix_right
				ai = current_node.air
				current_node = root.left
			else:
				A = current_node.matrix_right
				ai = current_node.ail
				current_node = current_node.right

# Calculate priority value, set count ++
		count = count + 1
		priority_value = priority(root.direction, root.median, q)

# Sort the rows of A in increasing order according to distance from q_not and let a have sorted indecies
		distnaces = []
		for i in A:
			distnaces.append(distance(i, q_not))
		a = [i[0] for i in sorted(enumerate(distnaces), key=lambda x:x[1])]

# Set the tree with counts and indecies of points
		for index in a:
			B.append((ai[index],count))

# Create a structire with count and put it into queue with priority
		structure = (count,current_node)
		P.put(priority_value, structure)

	#	Leaf_q = indecies of S in leaf_node
	#	C_q = C_q union leaf_q 
	#	t = t - 1
	#	current_node = (P.extract_max).current_node
	#	P.extract_max.count delete from B
	#return C_q union all candidates from B