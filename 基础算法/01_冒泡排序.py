def BubbleSort(alist):
	n = len(alist)
	for j in range(0,n-1):
		# 这样的过程经历了多少次
		for i in range(n-1-j):
			# 从头走到尾
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

def BubbleSort2(alist):
	for j in range(len(alist)-1,0,-1):
		for i in range(j):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

alist = [3, 4, 5 ,6 ,8 ,9 ,0]
# print(BubbleSort(alist))
print(alist)
print(BubbleSort2(alist))