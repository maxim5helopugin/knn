from queue import PriorityQueue
import numpy as np

def priority(U, v, q):
	return np.linalg.norm(v - np.dot(U,q))

def distance(x, q):
	return np.linalg.norm(x-q)

def guided_search(root, q, t, vectors):
	C_q = []
	B = [] # needs to be bst
	B_l = []
	A = None
	ai = None
	ai_l = None
	L_q = []
		
	P = PriorityQueue()
	count = 0
	q_not = []
# Get independent random vectors, create a set q_not
	for vector in vectors:
		q_not.append(np.dot(vector,q))

# Current node = root 
	current_node = root

	while t > 0:
		while not current_node.isleaf:
			if np.dot(current_node.direction, q) < current_node.median:
				A = current_node.matrix_right
				ai = current_node.air
				ai_l = current_node.air_l
				current_node = current_node.left
			else:
				A = current_node.matrix_left
				ai = current_node.ail
				ai_l = current_node.ail_l
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
				B_l.append((ai_l[index], count))

# Create a structire with count and put it into queue with priority
			P.put((priority_value, (count,current_node)))

		for point in current_node.data:
			C_q.append(point)

		for label in current_node.labels:
			L_q.append(label)

		t = t - 1

		temp = P.get()
		current_node = temp[1][1] 

		B = [x for x in B if x[1] != temp[1][0]]
		B_l = [x for x in B_l if x[1] != temp[1][0]]

	for i in range(0, len(B)):
		C_q.append(B[i][0])
		L_q.append(B_l[i][0])

	return np.stack(C_q), np.array(L_q)