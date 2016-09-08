def partition(arr, left, right):
    pivot = arr[(left+right) // 2]
    while left <= right:
		while arr[left] < pivot:
			left += 1
		while arr[right] > pivot:
			right -= 1
		if left <= right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
    return left
def quicksort(arr, left, right):
    index = partition(arr, left, right)
    if index - 1 > left:
        quicksort(arr, left, index - 1)
    if index < right:
        quicksort(arr, index, right)

arr = [1,5,4,34,7,3,5,3,7,3,5,3,7,3]
quicksort(arr, 0, len(arr)-1)
print arr