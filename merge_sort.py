from random import randint
import time
def merge(a, b):
    res = []
    while len(a) > 0 and len(b) > 0:
        if a[0] <= b[0]:
            res.append(a[0])
            del a[0]
        else:
            res.append(b[0])
            del b[0]
    if len(a) > 0:
        res += a
    if len(b) > 0:
        res += b
    return res

def sort(arr):
    #print arr
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    
    left = sort(arr[0:mid])
    right = sort(arr[mid:])
    return merge(left, right)


arr = [randint(0,10000) for i in xrange(10000)]
start = time.time()
res = sort(arr)
end = time.time()
print "time :", end - start
print res
