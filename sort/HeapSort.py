def max_heapfiy(a, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and a[child] < a[child + 1]:
            child = child + 1
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
        else:
            break


def heap_sort(a):
    n = len(a)
    first = n / 2 - 1 #因二叉树  n0+n1+n2 = n1+ 2n2 +1 得到 n0 = n2+1, 故 n = n0+ [1|0] + n0 -1 , 故 n0 = n/2 -1
    for start in range(first, -1, -1):
        max_heapfiy(a, start, n - 1)
    for end in range(n - 1, 0, -1):
        a[end], a[0] = a[0], a[end]
        max_heapfiy(a, 0, end - 1)
    return a
