"""
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {']': '[', '}': '{', ')': '('}
        for c in s:
            if c in dict.values():
                stack.append(c)
            elif c in dict.keys():
                if stack == [] or dict[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []
