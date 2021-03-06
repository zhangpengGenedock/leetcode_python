"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation/2
        
        tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
        For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

        len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
        len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
        len = 3   :      [4, 5, 6]            => tails[2] = 6
        We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

        Each time we only do one of the two:

        (1) if x is larger than all tails, append it, increase the size by 1
        (2) if tails[i-1] < x <= tails[i], update tails[i]
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

    def lengthOfLIS2(self, nums):
        """
        https://discuss.leetcode.com/topic/28916/python-dp-with-o-n-2-binary-search-with-o-nlogn
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
