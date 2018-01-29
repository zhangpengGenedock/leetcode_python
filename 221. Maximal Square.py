# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        offical solution: https://leetcode.com/problems/maximal-square/solution/   很详细in java
        personal https://leetcode.com/problems/maximal-square/discuss/61925/
        还有个o(n) space的解法
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0
        ans = max([max(x) for x in dp])
        return ans ** 2

