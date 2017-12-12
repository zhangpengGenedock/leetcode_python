# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        while n > 0:
            n /= 5
            r += n
        return r

    def trailingZeroes2(self, n):
        return 0 if n == 0 else n / 5 + self.trailingZeroes2(n / 5)
