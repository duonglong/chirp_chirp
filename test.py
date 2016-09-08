def arrayMode(sequence):
    max = 0
    count = {}
    for i in sequence:
        if i not in count:
            count[i]=0
        count[i] = count[i] + 1
    print count
    for value in count:
    	print value, count[value]
        if value > max:
            max = count[value]
    return max
print arrayMode([1, 3, 3, 3,3 , 1])
