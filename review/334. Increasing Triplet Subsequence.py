class Solution(object):
    def increasingTriplet(self, nums):
        """
        https://discuss.leetcode.com/topic/39807/python-easy-o-n-solution/2
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('Inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
