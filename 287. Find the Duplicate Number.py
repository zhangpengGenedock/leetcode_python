class Solution(object):
    def findDuplicate(self, nums):
        """
        offical solution: https://leetcode.com/problems/find-the-duplicate-number/solution/
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def findDuplicate2(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    def findDuplicate3(self, nums):
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
