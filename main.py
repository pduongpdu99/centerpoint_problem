from Node import *
from dfs import *
from bfs import *
from intergrate_bfs_dfs import *

import numpy as np
from time import sleep

import os
import sys

def main():
	# amount of node
	NODE_AMOUNT = 10

	#defined vectorize
	vNode = np.vectorize(Node)

	# init array Node
	init_array = np.arange(NODE_AMOUNT)

	#define node array
	nodes = np.empty(NODE_AMOUNT, dtype=object)
	nodes[:] = vNode(init_array)

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

	resultBFS = bfs_dfs(nodes)
	print([i.index for i in resultBFS])

if __name__ == "__main__":
	filename = str(sys.argv[0])

	# test syntax this current file
	# os.system('mypy ' + filename)

	main()


# start 