"""
https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        https://discuss.leetcode.com/topic/23559/pure-1d-dp-without-using-stack-python-with-detailed-explanation
        
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        :type s: str
        :rtype: int
        """
        dp = [0 for x in xrange(len(s))]
        max_to_now = 0
        for i in xrange(1, len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i - 1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = (0 if i < 2 else dp[i - 2]) + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if dp[i - 1] > 0:  # content within current matching pair is valid
                        # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now
