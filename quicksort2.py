def partition(arr, left, right):
    pivot = arr[(left + right)/2]
    i = left
    j = right
    while i<=j:
        while arr[i] < pivot:
            i = i + 1
        while arr[j] > pivot:
            j = j - 1
        if i <= j :
            arr[i], arr[j] = arr[j], arr[i]
            j = j - 1
            i = i + 1
    return i
def quicksort(arr, left, right):
    index = partition(arr, left, right)
    if left < index - 1:
        quicksort(arr, left, index - 1)
    if index < right:
        quicksort(arr, index, right)

arr = [1,67,4,6,3,5,6,4,5,6]
quicksort(arr, 0, len(arr)-1)
print arr
