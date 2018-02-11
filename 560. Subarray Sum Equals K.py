# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        personal solution: https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation
        discuss
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, sum, res = {0: 1}, 0, 0
        for v in nums:
            sum += v
            res += count.get(sum - k, 0)
            count[sum] = count.get(sum, 0) + 1
        return res
