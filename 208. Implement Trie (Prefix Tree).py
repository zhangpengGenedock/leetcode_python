# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class TrieNode:
    def __init__(self):
        import collections
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True


# solution from fastest submissions
class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for c in word:
            if c in node:
                node = node[c]
            else:
                node[c] = dict()
                node = node[c]
        node['term'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.trie
        for c in word:
            if c in node:
                node = node[c]
            else:
                return False
        return node.get('term') is not None

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.trie
        for c in prefix:
            if c in node:
                node = node[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
