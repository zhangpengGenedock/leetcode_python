# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""Given an array of integers, find out whether there are two distinct indices i and j in the array such that the 
absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k. 

"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
