class Solution(object):
    def lengthOfLIS(self, nums):
        """
        https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation/2
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
