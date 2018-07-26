alist = [132, 3, 4 ,2 ,55, 66, 5, 44, 4, 5]

def ShellSort(alist):
	n = len(alist)
	gap = n // 2
	times = 1
	while gap >= 1:
		for i in range(gap,n):
			for j in range(i,gap-1,-gap):# 出错点: 循环条件设置成了range(i,0,-gap), 导致下面的j-gap变成负数, 而列表可以负索引, 导致错误的取值; 而我们知道, 进行判定都是j-gap, 所以当j走到gap的时候, 就可以遍历所有的情况了
				print(j)
				if alist[j] < alist[j-gap]:  
					print(alist, end=' ')
					print('alist {0}({1}) <-> {2}({3})'.format(j, alist[j], j-gap, alist[j-gap]))
					alist[j], alist[j-gap] = alist[j-gap], alist[j]
					print(alist)
				else:
					break
			print()
		print("第{0}次遍历".format(times))
		times += 1
		gap //= 2
	return alist

# print(alist)
print(ShellSort(alist))
