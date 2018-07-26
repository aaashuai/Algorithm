class Node(object):
	def __init__(self, elem):
		self.elem = elem
		self.next = None

# node = Node(100)
# 先看怎么使用, 再回过头去创建

class SingleLinkList(object):
	'''单链表'''
	#方法都应该是对象方法
	#使用的时候都要创建实例对象来使用
	def __init__(self, node=None):
		# 自己内部的函数使用, 对外不暴露
		self.__head = node # 头节点指向第一个节点


	def is_empty(self):
		return self.__head == None
	
	def length(self):
		# cur游标, 用来移动遍历节点
		cur = self.__head  # 指向第一个节点
		# count 记录数量
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count
	
	def travel(self):
		cur = self.__head  # 指向第一个节点
		while cur != None:
			print(cur.elem, end=' ')
			cur = cur.next
		print()
		
	def add(self, item):
		node = Node(item)
		node.next = self.__head
		self.__head = node


	def append(self, item):
		# item 只是具体的数据, 并不是节点
		node = Node(item)
		# 首先要遍历到最后, 尾节点指向新的区域
		cur = self.__head
		if self.is_empty():
			self.__head = node
		else:
			while cur.next != None:
				cur = cur.next
			cur.next = node		

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
		pre = None
		cur = self.__head
		while cur != None:
			if cur.elem != item:
				pre = cur
				cur = cur.next
			else:
				# 判断此节点是否是头结点
				if pre == None:
					self.__head = cur.next
				else:
					pre.next = cur.next
				break
		
		


	def search(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
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
	# 8 2 29 3 4 5
	ll.insert(5, 2229) 
	ll.travel()
	# 8 2 29 3 4 2229 5
	ll.insert(222, 2119)
	ll.insert(222, 2119)
	ll.travel()
	# 8 2 29 3 4 2229 5 2119 2119
	ll.remove(2119)
	ll.travel()



# 1, 每次构造函数的时候, 先进行通解, 在找特解 
# 比如先把非特殊情况的数据处理解决了, 再看特殊情况下, 普通的数据处理是否还有效
# 
# 2, 在类中,如果新定义的方法可以用到已经定义的方法, 那么毫不犹豫的用吧
# 
# 3, 后继结点: 对于当前节点的下一个节点
# 
# 4, 优化代码-> 头插, 尾插, 中间插 的时间复杂度 1 n n
# 
# 链表不能向顺序表那样直接找到某个值, 只能一个一个去寻找
# 为什么还用链表, 存储数据时内存可以分散存储
# 比较:
# 顺序表 : 
# 优点 : 
# 	存取元素的时候可以以O(1)的复杂度进行操作
# 缺点 : 
# 	对于顺序表, 存储空间必须是连续的, 而且当一次开辟的空间用完了, 需要集体迁移, 而且如果没有那么大的连续空间就无法存储
# 	
# 链表:
# 	优点:
# 		可以充分的利用分散的内存空间
# 	缺点:
# 		由于需要多存一个地址, 所以存储的开销较大, 而且进行存取操作的时候, 只能以O(n)复杂度进行遍历
# 
# 对于两者对插入的复杂度不同点:
# 	链表是在于遍历, 顺序表示在于数据搬迁