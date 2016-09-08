def partition(a, i, j):
    pivot = (i + j) // 2
    while i <= j:
        while a[i] < a[pivot]:
            i += 1
        while a[j] > a[pivot]:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    return i
def quicksort(a, left, right):
    index = partition(a, left, right)
    print a
    print "a[%s] = %s" % (index, a[index])
    if index - 1 > left:
        quicksort(a, left, index - 1)
    if index < right:
        quicksort(a, index, right)

a= [32,6,64,2,432,6,345,234,63,234,45,234,234,63128,5,3,3,6,3,4,6]
quicksort(a, 0, len(a)-1)
print a
