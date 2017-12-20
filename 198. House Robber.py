# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
#  the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
#  it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
# money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        """
        solution: https://leetcode.com/problems/house-robber/solution/
        时间复杂度： o(n)
        空间复杂度： o(1)
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now
