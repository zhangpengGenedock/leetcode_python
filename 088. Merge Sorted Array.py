"""
https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        k = n - 1
        for i in range(m + n - 1, -1, -1):
            if j < 0:
                nums1[i] = nums2[k]
                k -= 1
            elif k < 0:
                nums1[i] = nums1[j]
                j -= 1
            elif nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1

    def merge2(self, nums1, m, nums2, n):
        """
        https://discuss.leetcode.com/topic/19513/beautiful-python-solution
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

    def merge3(self, nums1, m, nums2, n):
        """
        https://discuss.leetcode.com/topic/19513/beautiful-python-solution
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        """
        while n > 0:
            if m <= 0 or nums2[n - 1] >= nums1[m - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


if __name__ == '__main__':
    nums1 = [0]
    Solution().merge(nums1, 0, [1], 1)
    print nums1
    nums1 = [0]
    Solution().merge2(nums1, 0, [1], 1)
    print nums1
