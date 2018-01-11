# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if 
possible. 

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        from offical solutions
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def self_dividing(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True

        ans = []
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)
        return ans

    def selfDividingNumbers2(self, left, right):
        """
        from best answers
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def is_self_dividing(num):
            temp = num
            while temp > 0:
                current = temp % 10
                if current == 0 or num % current != 0:
                    return False
                temp //= 10
            return True

        return filter(is_self_dividing, range(left, right + 1))
