"""
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = cmp(x, 0)
        r = int(s * x[::-1])
        return s * r * (r < 2 ** 31)

    def revers2(self, x):
        """
        If overflow exists, the new result will not equal previous one.
        No flags needed. No hard code like 0xf7777777 needed.
        :param x: 
        :return: 
        """
        result = 0
        while x != 0:
            tail = x % 10
            new_result = result * 10 + tail
            if (new_result - tail) / 10 != result:
                return 0
            result = new_result
            x = x / 10
