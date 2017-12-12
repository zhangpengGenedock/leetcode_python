# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return ''.join(nums).lstrip('0') or '0'
