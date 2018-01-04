# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        offical solution: https://leetcode.com/problems/summary-ranges/solution/ 
        someone solution: https://leetcode.com/problems/summary-ranges/discuss/63393
        :type nums: List[int]
        :rtype: List[str]
        """
        begin, res = 0, []
        strout = lambda b, e: str(b) + '->' + str(e) if b != e else str(b)
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                res.append(strout(nums[begin], nums[i - 1]))
                begin = i
        return res
