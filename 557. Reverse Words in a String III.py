class Solution(object):
    def reverseWords(self, s):
        """
        solution: https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/101909/
        :type s: str
        :rtype: str
        """
        return ' '.join(x[::-1] for x in s.split())

    def reverseWords2(self, s):
        return ' '.join(s.split()[::-1])[::-1]
