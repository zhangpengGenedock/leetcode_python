# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'


# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        https://discuss.leetcode.com/topic/8805/4-lines-python-solution/2
        :type s: str
        :rtype: List[str]
        """
        import collections
        sequences = collections.defaultdict(int)
        for i in range(len(s)):
            sequences[s[i:i + 10]] += 1
        return [key for key, value in sequences.iteritems() if value > 1]

    def findRepeatedDnaSequences2(self, s):
        """
        fastest answer retrieve from leetcode submission
        :param s: 
        :return: 
        """
        if not s:
            return []

        r, p = set(), set()
        for i in xrange(len(s) - 9):
            t = s[i:i + 10]
            if t in p:
                r.add(t)
            else:
                p.add(t)

        return list(r)
