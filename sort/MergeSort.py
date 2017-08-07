def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[l]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) / 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


# 迭代实现
def merge_sort(a):
    length = len(a)
    step = 1
    result = []
    while step < length:
        for left in range(0, length - step, 2 * step):
            result += merge(a[left: left + step], a[left + step:min(left + 2 * step, length)])
            a = a[0:left] + result + a[min(left + 2 * step, length):]
        step *= 2
    return a
