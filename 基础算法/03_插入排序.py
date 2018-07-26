alist = [132, 3, 4 ,2 ,55, 66, 5, 44, 4, 1, 2, 5]
blist = [1, 2, 2, 3, 4, 4, 5, 5, 44, 55, 66, 132]
def InsertSort(alist):
	n = len(alist)
	for i in range(1, n):
		for j in range(i):
			print(j)
			if alist[i-j] < alist[i-1-j]:
				alist[i-1-j], alist[i-j] = alist[i-j], alist[i-1-j]
			else:
				break
		print()
	return alist

def InsertSort2(alist):
	n = len(alist)
	for i in range(1, n):
		for j in range(i,0,-1):
			# i = 5 j = 5 4 3 2 1
			print(j)
			if alist[j] < alist[j-1]:
				alist[j], alist[j-1] = alist[j-1], alist[j]
			else:
				break
		print()
	return alist
	
print(InsertSort2(blist))