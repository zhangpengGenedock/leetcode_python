# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the 
number I picked. 

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

Credits:
Special thanks to @agave and @StefanPochmann for adding this problem and creating all test cases.


"""


class Solution(object):
    def getMoneyAmount(self, n):
        """
        offical solution: https://leetcode.com/problems/guess-number-higher-or-lower-ii/solution/
        personal solution: https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84769/Two-Python-solutions
        brilliant
        :type n: int
        :rtype: int
        """
        need = [[0] * (n + 1) for _ in range(n + 1)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi]) for x in range(lo, hi))
        return need[1][n]

    def getMoneyAmount(self, n):
        """
        from submission (fast)
        :param n: 
        :return: 
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def dphelper(s, e):
            if s >= e:
                return 0
            if dp[s][e]:
                return dp[s][e]
            ret = float('inf')
            mid = (s + e) / 2
            for m in range(mid, e + 1):
                tmp = m + max(dphelper(s, m - 1), dphelper(m + 1, e))
                ret = min(ret, tmp)
            dp[s][e] = ret
            return ret

        return dphelper(1, n)
