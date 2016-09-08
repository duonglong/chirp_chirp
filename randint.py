import random
def shuffle(ar, n):
    return [ar[random.randint(0,len(ar)-1)] for k in xrange(n)]
print shuffle([1,6,3,1,5,2,4,9,7,7,5,8], 3)
