# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        k + (n-k)logk
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]

    def findKthLargest2(self, nums, k):
        """
        o(n)
        :param nums: 
        :param k: 
        """
        pos = self.partition(nums, 0, len(nums) - 1)
        if pos > len(nums) - k:
            return self.findKthLargest2(nums[:pos], k - (len(nums) - pos))
        elif pos < len(nums) - k:
            return self.findKthLargest2(nums[pos + 1:], k)
        else:
            return nums[pos]

    def partition(self, nums, l, r):
        pivot = nums[l]
        lo = l
        for i in xrange(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo
