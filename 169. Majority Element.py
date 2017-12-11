# -*- coding:utf-8 -*-
import collections

__author__ = 'zhangpeng'


# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


class Solution:
    def majorityElement(self, nums):
        """
        https://leetcode.com/problems/majority-element/solution/
        :type nums: List[int]
        :rtype: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

    def mjorityElement3(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    s = Solution()
    print s.majorityElement2([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7])
    print s.majorityElement2([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5])
    # 因为下面的数组不存在major element，不符合条件，所以得出的结果是错的。
    print s.majorityElement2([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 6, 6, 6, 6])
