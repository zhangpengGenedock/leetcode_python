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
