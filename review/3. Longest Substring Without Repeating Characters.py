class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        https://discuss.leetcode.com/topic/11632/a-python-solution-85ms-o-n
        :type s: str
        :rtype: int
        """
        start = max_length = 0
        used_char = {}

        for i in range(len(s)):
            if s[i] in used_char and start <= used_char[s[i]]:
                start = used_char[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used_char[s[i]] = i
        return max_length
