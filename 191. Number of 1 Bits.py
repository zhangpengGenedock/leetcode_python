# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
 Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

 For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        https://leetcode.com/problems/number-of-1-bits/solution/
        https://discuss.leetcode.com/topic/28481/python-2-solutions-one-naive-solution-with-built-in-functions-one-trick-with-bit-operation/2
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c

    def hammingweight2(self, n):
        return bin(n).count('1')
