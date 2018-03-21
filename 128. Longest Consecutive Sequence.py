"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers = set(nums)
        max_len = 0
        while numbers:
            m = n = numbers.pop()
            length = 1
            while m - 1 in numbers:
                numbers.remove(m - 1)
                m -= 1
                length += 1
            while n + 1 in numbers:
                numbers.remove(n + 1)
                n += 1
                length += 1
            max_len = max(max_len, length)
        return max_len

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
