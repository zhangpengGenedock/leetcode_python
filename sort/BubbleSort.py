def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1, n - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
    return array


# 优化版本：

def bubble_sort2(array):
    n = len(array)
    for i in range(n):
        flag = 1
        for j in range(1, n - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                flag = 0
        if flag:
            break
    return array


def bubble_sort3(array):
    n = len(array)
    k = n
    for i in range(n):
        flag = 1
        for j in range(1, k):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                k = j
                flag = 0
        if flag:
            break
    return array
