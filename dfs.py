import numpy as np
# depth first search
def dfs(nodes):
	# init array visited for mark visit when read location
	result = np.empty(0,dtype=object)
	length = len(nodes)

	# init memory 
	empty_size = 0
	memory = np.empty(empty_size,dtype=object)
	queue = np.empty(empty_size, dtype=object)

	firstnode = nodes[0]
	memory = np.append(memory, firstnode)
	queue = np.append(queue, firstnode)

	jump = 0
	# start deep
	while len(queue) != 0:
		consider_node = queue[0]
		children_length = len(consider_node.childrens)

		if children_length != 0:
			queue = np.insert(queue,0, consider_node.childrens[0])
			consider_node.childrens = np.delete(consider_node.childrens, 0)
			children_length = len(consider_node.childrens)
		else:
			result = np.insert(result, 0, queue[0])
			queue = np.delete(queue, 0)
	return result