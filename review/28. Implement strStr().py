class Solution(object):
    def strStr(self, haystack, needle):
        """
        https://discuss.leetcode.com/topic/29848/my-answer-by-python
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
