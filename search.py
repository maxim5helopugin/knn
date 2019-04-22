# Maxim Shelopugin
#
# Prioritiezed search with auxiliary information

from queue import PriorityQueue
import numpy as np

# Calculate the priority
def priority(U, v, q):
	return np.linalg.norm(v - np.dot(U,q))

# Get the distance between two vectors
def distance(x, q):
	return np.linalg.norm(x-q)

# Search method
def guided_search(root, q, t, vectors):
	target_set = []
	target_labels = []
	rpt_set = []
	rpt_set_labels = []
	matrix = None
	proxy = None
	proxy_labels = None
	
		
	priority_queue = PriorityQueue()
	count = 0
	q_not = []

# Get independent random vectors, create a set q_not
	for vector in vectors:
		q_not.append(np.dot(vector,q))

# Current node = root 
	current_node = root

# Do t iterations
	while t > 0:
		while not current_node.isleaf:
			if np.dot(current_node.direction, q) < current_node.median:
				matrix = current_node.matrix_right
				proxy = current_node.air
				proxy_labels = current_node.air_l
				current_node = current_node.left
			else:
				matrix = current_node.matrix_left
				proxy = current_node.ail
				proxy_labels = current_node.ail_l
				current_node = current_node.right

# Calculate priority value, set count ++
			count = count + 1
			priority_value = priority(root.direction, root.median, q)

# Sort the rows of matrix in increasing order according to distance from q_not and let a have sorted indecies
			distnaces = []
			for i in matrix:
				distnaces.append(distance(i, q_not))
			a = [i[0] for i in sorted(enumerate(distnaces), key=lambda x:x[1])]

# Set the tree with counts and indecies of points
			for index in a:
				rpt_set.append((proxy[index],count))
				rpt_set_labels.append((proxy_labels[index], count))

# Create a structire with count and put it into queue with priority
			priority_queue.put((priority_value, (count,current_node)))

		for point in current_node.data:
			target_set.append(point)

		for label in current_node.labels:
			target_labels.append(label)

		t = t - 1

# Prune out the nodes which do not add any info
		temp = priority_queue.get()
		current_node = temp[1][1] 

		rpt_set = [x for x in rpt_set if x[1] != temp[1][0]]
		rpt_set_labels = [x for x in rpt_set_labels if x[1] != temp[1][0]]

# Get the set of all candidates
	for i in range(0, len(rpt_set)):
		target_set.append(rpt_set[i][0])
		target_labels.append(rpt_set_labels[i][0])

	return np.stack(target_set), np.array(target_labels)