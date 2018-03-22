""" Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

 Try to solve it in linear time/space.

 Return 0 if the array contains less than 2 elements.

 You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

 Credits:
 Special thanks to @porker2008 for adding this problem and creating all test cases.

"""


class Solution(object):
    """
    官方答案
    https://leetcode.com/problems/maximum-gap/solution/
    """

    def radix_sort(self, A):
        for k in range(10):
            s = [[] for _ in xrange(10)]
            for i in A:
                s[i / (10 ** k) % 10].append(i)
            A = [a for b in s for a in b]
        return A

    def maximumGap(self, nums):
        """
        https://discuss.leetcode.com/topic/13784/simple-radix-sort-solution-in-python/2
        
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        A = self.radix_sort(nums)
        return max(A[i] - A[i - 1] for i in range(1, len(nums)))

    def maximumGap2(self, num):

        """
        https://discuss.leetcode.com/topic/9626/python-bucket-sort-from-official-solution/2
        
        :param num: 
        :return: int
        """
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        import math
        size = math.ceil((b - a) / (len(num) - 1))
        bucket = [[None, None] for _ in range((b - a) // size + 1)]
        for n in num:
            b = bucket[(n - a) // size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))
