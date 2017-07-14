import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        https://discuss.leetcode.com/topic/19721/share-my-two-python-solutions-a-very-concise-one-12-lines-160ms-and-an-optimized-solution-100ms
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        wordSet.discard(beginWord)
        while front:
            front = wordSet & (set(
                word[:index] + ch + word[index + 1:] for word in front for index in range(len(beginWord)) for ch in
                list(string.lowercase)))
            if front & back:
                return length
            length += 1
            if len(front) > len(back):
                front, back = back, front
            wordSet -= front
        return 0
