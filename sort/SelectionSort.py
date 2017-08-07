def select_sort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min]
    return array
