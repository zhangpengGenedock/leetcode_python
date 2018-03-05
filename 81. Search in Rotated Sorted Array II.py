"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0: return False
        start, end = 0, len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                start, end = i + 1, i + len(nums)
        while start <= end:
            mid = start + (end - start) / 2
            cur = nums[mid % len(nums)]
            if cur == target:
                return True
            elif cur > target:
                end = mid - 1
            else:
                start = mid + 1
        return False


if __name__ == '__main__':
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 5) == True
