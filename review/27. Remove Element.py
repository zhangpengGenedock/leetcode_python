"""
https://leetcode.com/problems/remove-element/description/

Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        https://discuss.leetcode.com/topic/1228/my-solution-for-your-reference
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[begin] = nums[i]
                begin += 1
        return begin
