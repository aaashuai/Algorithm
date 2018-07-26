def quick_sort(array, beg, end):
    if beg >= end:
        return
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end
    while left < right:
        while left <= right and array[left] < pivot:
            left += 1
        while left <= right and array[right] >= pivot:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[right], array[pivot_index] = array[pivot_index], array[right]
    
    quick_sort(array, beg, right-1)  # 难点
    quick_sort(array, right+1, end)
    return array


def test_quick_sort():
    import random
    array = [i for i in range(10)]
    random.shuffle(array)
    n = len(array) - 1
    print(array)
    print(quick_sort(array, 0, n))


if __name__ == "__main__":
    test_quick_sort()