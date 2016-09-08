import random
def partition(a, left, right):
    i = left
    j = right
    pivot = a[(left + right) / 2];
    while (i<=j):
        while a[i] < pivot:
            i = i + 1            
        while a[j] > pivot:
            j = j - 1
        if i <= j:
            print "Pivot: %s, Swaping a[%s] : %s with a[%s]:%s" % (pivot, i, a[i], j, a[j])
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
    return i
def quicksort(a, left, right):
    index = partition(a, left, right)
    print "index %s :" % index, a
    
    if left < index - 1:
        quicksort(a, left, index - 1)
    if index < right:
        quicksort(a, index, right)
a = [int(1000*random.random()) for i in xrange(10)]
print a
quicksort(a, 0 , len(a)-1)
#print a

