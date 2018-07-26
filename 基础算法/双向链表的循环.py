class Node(object):
	def __init__(self, value=None, prev=None, next=None):
		self.value, self.prev, self.next = value, prev, next

class CircleDoubleLinked(object):
	def __init__(self):
		node = Node()
		node.prev, node.next = node, node
		self.rootnode = node

	def headnode(self):
		return self.rootnode.next

	def tailnode(self):
		return self.rootnode.prev

	def remove(self, node):
		if node is self.rootnode:
			return
		else:
			node.prev.next = node.next
			node.next.prev = node.prev

	def append(self, node):
		tailnode = self.tailnode()
		tailnode.next = node
		node.next = self.rootnode
		self.rootnode.prev = node
	
	def travel(self):
		cur = self.rootnode  # 指向第一个节点
		while cur.next != self.rootnode:
			print(cur.value, end=' ')
			cur = cur.next
		# 退出循环, 退出尾节点, 但尾节点元素尚未打印
		print(cur.value)


if __name__ == '__main__':
	dl = CircleDoubleLinked()
	dl.append(Node(3))
	dl.travel()
	dl.append(Node(5))
	dl.travel()