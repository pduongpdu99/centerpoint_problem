import numpy as np

# Breadth first search
def bfs(nodes):
	# init array visited for mark visit when read location
	amount = len(nodes)
	visited = np.full(amount, False)
	result = []

	queue = []
	queue = np.append(queue, nodes[0])
	while len(queue) != 0:
		node = queue[0]
		result.append(node)
		queue = np.delete(queue, 0)
		for i in node.childrens:
			if visited[i.index] == False:
				queue = np.append(queue, i)
				visited[i.index] = True
	return result