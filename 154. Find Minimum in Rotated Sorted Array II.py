# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        beg, end = 0, len(nums) - 1
        while beg <= end:
            while beg < end and nums[beg] == nums[beg + 1]:
                beg += 1
            while end > beg and nums[end] == nums[end - 1]:
                end -= 1
            if beg == end:
                return nums[beg]
            mid = (beg + end) / 2
            if nums[mid] > nums[end]:
                beg = mid + 1
            else:
                end = mid
        return nums[beg]

    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r = r - 1
        return nums[l]
