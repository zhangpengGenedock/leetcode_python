"""
https://leetcode.com/problems/word-ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""
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
