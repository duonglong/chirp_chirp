def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while(high >= low):
        mid = (low + high) // 2
        if (arr[mid] == value):
            return "Found at %s" % mid
        
        if arr[mid] < value:
            low = mid + 1
        if arr[mid] > value:
            high = mid - 1
    return "Search ended"

a= [1,2,3,3,4,5,6,7,8,9]
print binary_search(a, 9)
