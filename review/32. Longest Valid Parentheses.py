class Solution(object):
    def longestValidParentheses(self, s):
        """
        https://discuss.leetcode.com/topic/23559/pure-1d-dp-without-using-stack-python-with-detailed-explanation
        :type s: str
        :rtype: int
        """
        dp = [0 for _ in xrange(len(s))]
        max_to_now = 0
        for i in xrange(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (0 if i < 2 else dp[i - 2]) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if dp[i - 1] > 0:
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now
