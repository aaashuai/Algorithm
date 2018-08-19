'''
# 递归版本 
def binary_search(num, alist，left, right):
	if left >= right:
		return False

	mid = (left+right) // 2
	if num == alist[mid]:
		return True
	elif num < alist[mid]:
		return binary_search(num, alist[left:mid], left, mid-1)
	else:
		return binary_search(num, alist[mid+1:right+1], mid+1, right)

alist = [i for i in range(0, 20, 3)]
print(alist)
n = len(alist) - 1
if binary_search(15, alist, 0, n):
	print('yes')\
else:
	print('no')


'''
'''
review:                              
import sys                                    
def binary_search(arr, num):
    n = len(arr)
    if n < 1:
        return False
    mid = n // 2
    if arr[mid] == num:
        return True
    elif arr[mid] < num:
        return binary_search(arr[mid+1:], num)
    else:
        return binary_search(arr[:mid], num)
	
arr = [i for i in range(3, 10, 2)]
num = int(sys.argv[1])
print(arr, num)
if binary_search(arr, num):
    print("yes")
else:
    print("NO")
'''
# 非递归版本


def binary_search_2(num, alist):
    n = len(alist)
    alist = alist
    mid = n // 2
    while n >= 1:
        if num == alist[mid]:
            return True
        elif num > alist[mid]:
            alist = alist[mid+1:]
            n = len(alist)
            mid = n // 2
        else:
            alist = alist[:mid]
            n = len(alist)
            mid = n // 2

    return False


alist = [i for i in range(0, 20, 3)]
print(alist)
n = len(alist) - 1
if binary_search_2(0, alist):
    print('yes')
else:
    print('no')
