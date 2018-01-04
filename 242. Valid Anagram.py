# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        offical solution: https://leetcode.com/problems/valid-anagram/solution/
        someone solution: https://leetcode.com/problems/valid-anagram/discuss/66499/
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def isAnagram3(self, s, t):
        dic1, dic2 = [0] * 26, [0] * 26
        for item in s:
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1
        return dic1 == dic2
