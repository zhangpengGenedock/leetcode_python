# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""


class Solution(object):
    def missingNumber(self, nums):
        """
        solution: https://leetcode.com/problems/missing-number/solution/
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

    def missingNumber2(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

    def missingNumber3(self, nums):
        return len(nums) * (len(nums) + 1) / 2 - sum(nums)
