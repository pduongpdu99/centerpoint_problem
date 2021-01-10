class Node:
	def __init__(self, index):
		self.index = index
		self.childrens = []

	def __str__(self):
		return "Node({})".format(self.index)


	def append(self, node):
		self.childrens.append(node)
		
