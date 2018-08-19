def quickSort(alist, first, last):
	if first >= last:
		return
	mid_value = alist[first]
	
	low = first
	high = last
	
	while low < high:
	    while low < high and alist[high] >= mid_value:
	        high -= 1
	    while low < high and alist[low] < mid_value:
	        low += 1
	    alist[low], alist[high] = alist[high], alist[low]

	alist[high] = mid_value

	# 对low左边的列表执行快速排序
	quickSort(alist, first, low-1)

	# 对low右边进行快排
	quickSort(alist, low+1, last)

	return alist
    

if __name__ == "__main__":
	alist = [132, 3, 4, 2, 55, 66, 5, 44, 4, 1, 2, 5]
	print(alist)
	quickSort(alist, 0, len(alist)-1)
	print(alist)
