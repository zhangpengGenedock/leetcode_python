class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in buff_dict:
                return [buff_dict[target - nums[i]], i]
            else:
                buff_dict[nums[i]] = i
