# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
https://leetcode.com/problems/daily-temperatures/description/

Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        offical solution: https://leetcode.com/problems/daily-temperatures/solution/
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
