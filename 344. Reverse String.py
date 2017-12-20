# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


class Solution(object):
    def reverseString(self, s):
        """
        solution: https://discuss.leetcode.com/topic/58719/python-3-solutions-recursive-classic-pythonic/2
        :type s: str
        :rtype: str
        """

        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l / 2:]) + self.reverseString(s[:l / 2])

    def reverseString2(self, s):
        r = list(s)
        i, j = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return ''.join(r)

    def reverseString3(self, s):
        return s[::-1]
