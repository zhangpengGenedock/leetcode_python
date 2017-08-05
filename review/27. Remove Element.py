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
