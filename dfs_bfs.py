import numpy as np
from Node import *
from time import sleep

import os
import sys

# Deep first search
def dfs(nodes):
	# init array visited for mark visit when read location

	result = np.empty(0,dtype=object)

	length = len(nodes)
	visited = np.full(length, True)
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
		# childrens = consider_node.childrens
		children_length = len(consider_node.childrens)
		print(consider_node, 
			[i.index for i in consider_node.childrens])

		if children_length != 0:
			queue = np.insert(queue,0, consider_node.childrens[0])
			consider_node.childrens = np.delete(consider_node.childrens, 0)
			children_length = len(consider_node.childrens)
		else:
			result = np.insert(result, 0, queue[0])
			queue = np.delete(queue, 0)
		# result = result[::-1]
		print("queue:",list(map(str, result)))
		sleep(.5)
	return result
	# Ok nhưng hơi bị ngược, nhưng không sao, bản chất vẫn đúng


# Breadth first search
def bfs(nodes):
	# init array visited for mark visit when read location
	visited = np.full(NODE_AMOUNT, True)

	return Node

def main():
	# amount of node
	NODE_AMOUNT = 10

	# step 1: create list node in node
	# This step is implemented in initiable a node
	# Thực hiện tại từng bước
	# Giới thiệu từng bước


	#defined vectorize
	vNode = np.vectorize(Node)

	# init array Node
	init_array = np.arange(NODE_AMOUNT)

	#define node array
	nodes = np.empty(NODE_AMOUNT, dtype=object)
	nodes[:] = vNode(init_array)
	
	for i in nodes:
		print(i)


	# complete init step
	nodes[0].append(nodes[1])
	nodes[0].append(nodes[2])
	nodes[1].append(nodes[3])
	nodes[1].append(nodes[4])
	nodes[1].append(nodes[5])
	nodes[2].append(nodes[6])
	nodes[2].append(nodes[7])
	nodes[3].append(nodes[8])
	nodes[4].append(nodes[9])

	resultDFS = dfs(nodes)
	print([i.index for i in resultDFS])

	# complete append node with figure 



if __name__ == "__main__":
	filename = str(sys.argv[0])

	# test syntax this current file
	# os.system('mypy ' + filename)

	main()


# start 