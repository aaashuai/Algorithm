# 归并排序

def merge_sort(alist):
	n = len(alist)
	if n <= 1:
		return alist   # 卡住点
	mid = n // 2
	# left 采用归并排序后形成的有序的新的列表
	left_li = merge_sort(alist[:mid])
	
	# left 采用归并排序后形成的有序的新的列表
	right_li = merge_sort(alist[mid:])
	
	# 将两个有序的子序列和并为一个新的整体
	# merge(left, right)
	left_pointer, right_pointer = 0, 0
	result = []

	while left_pointer < len(left_li) and right_pointer < len(right_li):
		if left_li[left_pointer] <= right_li[right_pointer]:
			result.append(left_li[left_pointer])
			left_pointer += 1
		else:
			result.append(right_li[right_pointer])
			right_pointer += 1

	result += left_li[left_pointer:]
	result += right_li[right_pointer:]

	return result


def test_merge_sort():
    import random
    array = [i for i in range(10)]
    random.shuffle(array)
    print(array)
    print(merge_sort(array))


if __name__ == "__main__":
    test_merge_sort()