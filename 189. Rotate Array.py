# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# public class Solution {
#     public void rotate(int[] nums, int k) {
#         k = k % nums.length;
#         int count = 0;
#         for (int start = 0; count < nums.length; start++) {
#             int current = start;
#             int prev = nums[start];
#             do {
#                 int next = (current + k) % nums.length;
#                 int temp = nums[next];
#                 nums[next] = prev;
#                 prev = temp;
#                 current = next;
#                 count++;
#             } while (start != current);
#         }
#     }
# }

class Solution(object):
    def rotate(self, nums, k):
        """
        solution:
        https://leetcode.com/problems/rotate-array/solution/
        
        https://discuss.leetcode.com/topic/96450/my-interpretation-proof-of-the-cyclic-replacements-method-in-editorial-solution/2
        该链接有对于平移详细的解释
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, 0, end - k + 1)
        self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate2(self, nums, k):
        k, count = k % len(nums), 0
        start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while start != current:
                next = (current + k) % len(nums)
                temp = nums[next]
                nums[next] = prev
                prev = temp
                current = next
                count += 1
