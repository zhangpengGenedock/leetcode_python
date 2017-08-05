class Solution(object):
    def search(self, nums, target):
        """
        https://discuss.leetcode.com/topic/13096/python-binary-search-solution-o-logn-48ms
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
