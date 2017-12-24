# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# For example:
#
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
#
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?


class Solution(object):
    def addDigits(self, num):
        """
        solution:
        https://discuss.leetcode.com/topic/21498/accepted-c-o-1-time-o-1-space-1-line-solution-with-detail-explanations/2
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else 1 + (num - 1) % 9
