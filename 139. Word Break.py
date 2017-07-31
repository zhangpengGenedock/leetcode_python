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
