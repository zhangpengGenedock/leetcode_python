# -*- coding:utf-8 -*-

__author__ = 'zhangpeng'

"""You are given coins of different denominations and a total amount of money amount. Write a function to compute the 
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any 
combination of the coins, return -1. 

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        offical java solution: https://leetcode.com/problems/coin-change/solution/
        personal discuss solution: https://leetcode.com/problems/coin-change/discuss/77372/
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in xrange(1, amount + 1):
            dp[i] = min(dp[i - c] if i - c >= 0 else MAX for c in coins) + 1
        return [dp[amount], -1][dp[amount] == MAX]

    def coinChange2(self, coins, amount):
        """
        回溯法
        from submissions
        :param coins: 
        :param amount: 
        :return: 
        """
        coins.sort(reverse=True)
        lenc, self.res = len(coins), 2 ** 31 - 1

        def dfs(s, remain, count):
            if remain == 0:
                self.res = min(count, self.res)
            for i in range(s, lenc):
                if coins[i] <= remain < coins[i] * (self.res - count):
                    dfs(i, remain - coins[i], count + 1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2 ** 31 - 1 else -1
