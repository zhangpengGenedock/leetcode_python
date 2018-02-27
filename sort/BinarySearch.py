# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


def binary_search(num, l):
    low = 0
    high = len(l) - 1
    while low <= high:
        middle = (low + high) / 2
        if l[middle] > num:
            high = middle - 1
        elif l[middle] < num:
            low = middle + 1
        else:
            return middle
    return -1
