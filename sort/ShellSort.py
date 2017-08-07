def shell_sort(a):
    n = len(a)
    gap = n / 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j = j - gap
            a[j] = temp
        gap = gap / 2
    return a
