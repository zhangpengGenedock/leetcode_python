"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.


"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        offical solution 很不容易理解
        personal solution: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824
        tails[i]
        tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
        For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

        len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
        len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
        len = 3   :      [4, 5, 6]            => tails[2] = 6
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
