"""
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        https://discuss.leetcode.com/topic/7823/accpeted-python-dp-solution/2
        :type s: str
        :rtype: int
        """
        if s == '': return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i != 1 and '27' > s[i - 2:i] > '09':
                dp[i] += dp[i - 2]
        return dp[i]


if __name__ == '__main__':
    assert Solution().numDecodings('12') == 2
