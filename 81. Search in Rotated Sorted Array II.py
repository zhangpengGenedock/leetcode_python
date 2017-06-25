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
