# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray 
of which the sum ≥ s. If there isn't one, return 0 instead. 

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.


"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        personal solution: https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59093/Python-O(n)-and-O(n-log-n)-solution
        o(n)
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = 0
        result = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right - left + 1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0

    def minSubArrayLen2(self, target, nums):
        """
        o(nlogn)
        :param s: 
        :param nums: 
        :return: 
        """
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left
