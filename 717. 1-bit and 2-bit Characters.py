# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""We have two special characters. The first character can be represented by one bit 0. The second character can be 
represented by two bits (10 or 11). 

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. 
The given string will always end with a zero. 

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit ch

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.

"""

import json


class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1

    def isOneBitCharacter2(self, bits):
        """
        from fastest submissions
        len = 6
        0 1 2 3 4 5
        0 1 0 0 1 0
        思路：倒数两个出现的0之间1的个数奇偶决定
        :param bits: 
        :return: 
        """
        i = len(bits) - 2
        while i >= 0:
            if bits[i] == 0:
                break
            i -= 1
        return (len(bits) - i) % 2 == 0
