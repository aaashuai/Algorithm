flag = '*****************'

# 让单向列表的尾节点指向头结点
class Node(object):
	def __init__(self, elem):
		self.elem = elem
		self.next = None

# node = Node(100)
# 先看怎么使用, 再回过头去创建

class SingleLinkList(object):
	'''单向循环链表'''
	#方法都应该是对象方法
	#使用的时候都要创建实例对象来使用
	def __init__(self, node=None):
		# 自己内部的函数使用, 对外不暴露
		self.__head = node # 头节点指向第一个节点
		if node:
			node.next = node

	def is_empty(self):
		return self.__head == None
	
	def length(self):
		if self.is_empty():
			return 0
		# cur游标, 用来移动遍历节点
		cur = self.__head  # 指向第一个节点
		# count 记录数量
		count = 1
		# 单向循环列表不能选择 cur == self.__head 条件, 因外第一次就是, 也就意味着count 情况也会改变
		while cur.next != self.__head:
			count += 1
			cur = cur.next
		return count
	
	def travel(self):
		cur = self.__head  # 指向第一个节点
		if self.is_empty():
			 return
		while cur.next != self.__head:
			print(cur.elem, end=' ')
			cur = cur.next
		# 退出循环, 退出尾节点, 但尾节点元素尚未打印
		print(cur.elem)
		
	def add(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			cur.next = node
			node.next = self.__head
			self.__head = node


	def append(self, item):
		# item 只是具体的数据, 并不是节点
		node = Node(item)
		# 首先要遍历到最后, 尾节点指向新的区域
		cur = self.__head
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			while cur.next !=self.__head:
				cur = cur.next
			cur.next = node	
			node.next = self.__head	

	def insert(self, pos, item):
		'''
		:param pos 从0开始
		'''
		node = Node(item)
		pre = self.__head
		if pos <= 0:
			self.add(item)

		elif pos > self.length():
			self.append(item)

		else:
			count = 0
			while count < pos-1:
				count += 1
				pre = pre.next
			node.next = pre.next
			pre.next = node


	def remove(self, item):
		if self.is_empty():
			return
		pre = None
		cur = self.__head
		while cur.next != self.__head:
			if cur.elem == item:
				if pre == None:
					# 头结点
					# 找尾节点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					rear.next = cur.next
					self.__head = cur.next
					# 中间节点
				else:
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next

		if cur.elem == item:
				if pre == None:
					self.__head = None
				else:
					pre.next = cur.next
				


	def search(self, item):
		cur = self.__head
		if self.__head is None:
			return False
		while cur.next != self.__head:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		if cur.elem == item:
			return True
		return False

if __name__ == "__main__":
	ll = SingleLinkList()
	print(ll.is_empty())
	print(ll.length())

	ll.append(1)
	print(ll.is_empty())
	print(ll.length())

	ll.append(2)
	ll.append(3)
	ll.add(8)
	ll.append(4)
	ll.append(5)

	ll.travel()
	# 8 2 3 4 5
	ll.insert(2, 29)

	ll.travel()
	ll.insert(-1, 6)
	ll.travel()
	# 8 2 29 3 4 5
	ll.insert(-1, 2229) 
	ll.travel()
	# 8 2 29 3 4 2229 5
	ll.insert(222, 2119)
	ll.insert(222, 2119)
	ll.travel()
	# 8 2 29 3 4 2229 5 2119 2119
	ll.remove(2119)
	ll.travel()
	ll.remove(2229)
	ll.travel()
	ll.add('abc')
	ll.travel()


	