from queue import PriorityQueue
import numpy as np

def priority(U, v, q):
	return 1 / np.linalg.norm(v - np.dot(U,q))

def guided_search(root, q, t, vectors):
	#C_q = []
	#B = binary_search_tree
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
		print(A)
		#		Sort the rows of A in increasing order according to distance from q_not and let a have sorted indecies
		#		Insert {ai(a(1))...ai(a(c''))} into B with count
		#		struct = (count, current_node)
		#		P.insert(struct, priority_value)
		#	Leaf_q = indecies of S in leaf_node
		#	C_q = C_q union leaf_q 
		#	t = t - 1
		#	current_node = (P.extract_max).current_node
		#	P.extract_max.count delete from B
		#return C_q union all candidates from B