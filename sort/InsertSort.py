def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        if a[i] < a[i - 1]:
            temp = a[i]
            index = i
            for j in range(i - 1, -1, -1):
                if a[j] > temp:
                    a[j + 1] = a[j]
                    index = j
                else:
                    break
            a[index] = temp
    return a
