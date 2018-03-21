"""
https://leetcode.com/problems/word-break/description/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        TimeLimit Exceed
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        result = False
        for word in wordDict:
            if s.startswith(word):
                result |= self.wordBreak(s[len(word):], wordDict)
                if result:
                    break

        return result

    def wordBreak2(self, s, wordDict):
        """
        https://discuss.leetcode.com/topic/8109/simple-dp-solution-in-python-with-description/2
        :param s:
        :param wordDict:
        """
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i - len(w) + 1:i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i] = True
                    break
        return d[-1]
