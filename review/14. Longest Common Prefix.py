class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        https://discuss.leetcode.com/topic/6308/simple-python-solution
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ''
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
