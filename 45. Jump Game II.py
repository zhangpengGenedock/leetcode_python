# coding=utf-8

"""
https://leetcode.com/problems/jump-game-ii/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 该方法会超时
        import sys
        result = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                result[i] = sys.maxint
            else:
                result[i] = min(result[i + 1: nums[i] + i + 1]) + 1
        return result[0]

    def jump2(self, nums):
        """
        https://discuss.leetcode.com/topic/18815/10-lines-c-16ms-python-bfs-solutions-with-explanations/2
        :param nums: list
        :return: int
        """
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step


if __name__ == '__main__':
    assert Solution().jump([2, 3, 1, 1, 4]) == 2
    assert Solution().jump2([2, 3, 1, 1, 4]) == 2
