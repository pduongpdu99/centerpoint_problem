import numpy as np

def bfs_dfs(nodes):
	length = len(nodes)
	result = np.empty(0, dtype=object)
	queue = np.empty(0,dtype=object)

	firstnode = nodes[0]
	queue = np.append(queue, firstnode)

	while len(queue) != 0:
		node = queue[0]
		queue = np.delete(queue, 0)
		result = np.append(result, node)
		childrens = node.childrens
		for index in range(len(childrens)):
			queue = np.insert(queue, index, childrens[index])

	return result
