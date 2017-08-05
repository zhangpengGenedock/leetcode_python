class Solution(object):
    def longestPalindrome(self, s):
        """
        https://discuss.leetcode.com/topic/7144/python-o-n-2-method-with-some-optimization-88ms/2
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        max_len = 1
        start = 0
        for i in range(len(s)):
            if i - max_len - 1 >= 0 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]
