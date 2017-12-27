# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""Given an array of integers, find if the array contains any duplicates. Your function should return true if any 
value appears at least twice in the array, and it should return false if every element is distinct. """


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] += 1
            if dic[nums[i]] > 1:
                return True
        return False

    def containsDuplicate2(self, nums):
        return len(nums) != len(set(nums))
