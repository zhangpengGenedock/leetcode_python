def qsort(a, left, right):
    if left >= right:
        return a
    key = a[left]
    lp = left
    rp = right
    while lp < rp:
        while a[rp] >= key and lp < rp:
            rp -= 1
        while a[lp] <= key and lp < rp:
            lp += 1
        a[lp], a[rp] = a[rp], a[lp]
    a[left], a[lp] = a[lp], a[left]
    qsort(a, left, lp - 1)
    qsort(a, rp + 1, right)
    return a


def quick_sort(a):
    return qsort(a, 0, len(a) - 1)
