# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        pythonic solution
        :type x: int
        :type y: int
        :rtype: int
        """
        m = x ^ y
        n = 0
        while m:
            n += 1
            m &= m - 1
        return n

    def hammingDistance2(self, x, y):
        """
        hamming
        :param x: 
        :param y: 
        """
        return bin(x ^ y).count('1')
