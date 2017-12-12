# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

class Solution:
    def titleToNumber(self, s):
        """
        python2 版本
        答案参见: https://discuss.leetcode.com/topic/6458/my-solutions-in-3-languages-does-any-one-have-one-line-solution-in-java-or-c
        :param s: 
        :return: 
        """
        return reduce(lambda x, y: x * 26 + y, [ord(c) - ord('A') + 1 for c in s])
