#　广度遍历
class Node(object):
	def __init__(self, item):
		self.item = item
		self.lchild = None
		self.rchild = None

class Tree(object):
	def __init__(self):
		self.root = None
	def add(self, item):
		node = Node(item)
		if self.root is None:
			self.root = node
			return
		queue = [self.root]
		while queue:
			cur_node = queue.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				queue.append(cur_node.lchild)
			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else:
				queue.append(cur_node.rchild)

	def breath_travel(self):
		if self.root is None:
			return
		queue = [self.root]
		while queue:
			cur_node = queue.pop(0)
			print(cur_node.item)
			if cur_node.lchild:
				queue.append(cur_node.lchild)
			if cur_node.rchild:
				queue.append(cur_node.rchild)

if __name__ == "__main__":
	tree = Tree()
	tree.add(5)				
	tree.add(2)
	tree.add(5)
	tree.add(4)
	tree.add(5)
	tree.breath_travel()