"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
class Solution(object):

    def longestConsecutive2(self, nums):
        """
        sample 32 ms submission
        :param nums:
        :return:
        """
        nums = set(nums)
        max_length = 0
        for n in nums:
            if n + 1 not in nums:
                y = n - 1
                while y in nums:
                    y -= 1
                max_length = max(max_length, n - y)
        return max_length
