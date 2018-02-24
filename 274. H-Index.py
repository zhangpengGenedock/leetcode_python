# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
https://leetcode.com/problems/h-index/description/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""


class Solution(object):
    def hIndex(self, citations):
        """
        offical solution: https://leetcode.com/problems/h-index/solution/
        o(nlogn),o(1)
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        i = 0
        while i < len(citations) and citations[len(citations) - 1 - i] > i:
            i += 1
        return i

    def hIndex2(self, citations):
        """
        o(n) o(n)
        :param citations: 
        :return: 
        """
        n = len(citations)
        papers = [0] * (n + 1)
        for c in citations:
            papers[min(n, c)] += 1
        k = n
        s = papers[n]
        while k > s:
            k -= 1
            s += papers[k]
        return k
