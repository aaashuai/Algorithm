alist = [132, 3, 4 ,2 ,55, 66, 5, 44, 4, 1, 2, 5]
blist = [(2, 4), (2, 1), (2, 5), (3, 4), (1, 3),(5, 1), (11, 11), (1, 1), (3, 5)]
# 		 0    1  2  3  4   5   6   7
from timeit import Timer

def SelectSort():
	# alist = [132, 3, 4 ,2 ,55, 66, 5, 44, 4, 1, 2, 5]
	for j in range(len(alist)-1):
		# j 从 0 ~ n-2
		for i in range(j+1,len(alist)):
			# i从j的后一位开始
			if alist[j] > alist[i]:
				print(alist)
				alist[j], alist[i] = alist[i], alist[j]
				print(alist)
		print()
	return alist

# 真选择排序
def SelectSort2():
	# alist = [132, 3, 4 ,2 ,55, 66, 5, 44, 4, 1, 2, 5]
	for j in range(len(alist)-1):
		min_index = j
		# j 从 0 ~ n-2
		for i in range(j+1,len(alist)):
			# i从j的后一位开始
			if alist[min_index] > alist[i]:
				min_index = i
		alist[j], alist[min_index] = alist[min_index], alist[j]
		
	return alist

def SelectSort3(alist):
	n = len(alist)
	for j in range(n-1):
		max_index = 0
		# j 从 0 ~ n-2
		for i in range(1,n-j):
			# i从j的后一位开始
			if alist[max_index][0] < alist[i][0]:
				max_index = i
				print(alist[max_index][0])
		alist[n-1-j], alist[max_index] = alist[max_index], alist[n-1-j]
		
	return alist
timer1 = Timer('SelectSort()', 'from __main__ import SelectSort')
timer1 = Timer('SelectSort2()', 'from __main__ import SelectSort2')


if __name__ == '__main__':
	# print(SelectSort2(list(set(alist))))
	# print("S1 : ", timer1.timeit(1000000))
	# print("S2 : ", timer1.timeit(1000000))
	print(SelectSort3(blist))
	# [(2, 4), (2, 1), (2, 5), (3, 4), (1, 3),(5, 1), (11, 11), (1, 1), (3, 5)]
	# [(1, 1), (1, 3), (2, 5), (2, 1), (2, 4), (3, 5), (3, 4), (5, 1), (11, 11)]
	# 调换了应有的前后顺序, 不稳定的