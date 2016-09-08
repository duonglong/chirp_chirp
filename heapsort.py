def max_heapify(a, i, n):
    temp = a[i]
    j = 2 * i
    while j <= n:
        if j < n and a[j + 1] > a[j]:
            j = j + 1
        if temp > a[j]:
            break
        elif temp <= a[j]:
            a[j // 2] = a[j]
            j *= 2
    a[j // 2] = temp


def heapsort(a, n):
    for i in range(n, 1, -1):
        a[i], a[1] = a[1], a[i]
        max_heapify(a, 1, i - 1)


def build_maxheap(a, n):
    for i in range(n // 2, 0, -1):
        print(i)
        max_heapify(a, i, n)


a = [1, 54, 3, 5, 7, 5, 6, 8, 2, 6, 88]

build_maxheap(a, len(a) - 1)
heapsort(a, len(a) - 1)
print(a)
