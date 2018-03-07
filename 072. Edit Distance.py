"""
https://leetcode.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        This is a classic problem of Dynamic Programming. We define the state dp[i][j] to be the minimum number of 
        operations to convert word1[0..i - 1] to word2[0..j - 1]. The state equations have two cases: the boundary 
        case and the general case. Note that in the above notations, both i and j take values starting from 1. 

        For the boundary case, that is, to convert a string to an empty string, it is easy to see that the mininum 
        number of operations to convert word1[0..i - 1] to "" requires at least i operations (deletions). In fact, 
        the boundary case is simply: 

        dp[i][0] = i; dp[0][j] = j. Now let’s move on to the general case, that is, convert a non-empty word1[0..i - 
        1] to another non-empty word2[0..j - 1]. Well, let’s try to break this problem down into smaller problems (
        sub-problems). Suppose we have already known how to convert word1[0..i - 2] to word2[0..j - 2], which is dp[i 
        - 1][j - 1]. Now let’s consider word[i - 1] and word2[j - 1]. If they are euqal, then no more operation is 
        needed and dp[i][j] = dp[i - 1][j - 1]. Well, what if they are not equal? 

        If they are not equal, we need to consider three cases:

        Replace word1[i - 1] by word2[j - 1] (dp[i][j] = dp[i - 1][j - 1] + 1 (for replacement)); Delete word1[i - 1] 
        and word1[0..i - 2] = word2[0..j - 1] (dp[i][j] = dp[i - 1][j] + 1 (for deletion)); Insert word2[j - 1] to 
        word1[0..i - 1] and word1[0..i - 1] + word2[j - 1] = word2[0..j - 1] (dp[i][j] = dp[i][j - 1] + 1 (for 
        insertion)). Make sure you understand the subtle differences between the equations for deletion and 
        insertion. For deletion, we are actually converting word1[0..i - 2] to word2[0..j - 1], which costs dp[i - 
        1][j], and then deleting the word1[i - 1], which costs 1. The case is similar for insertion. 

        Putting these together, we now have:

        dp[i][0] = i;
        dp[0][j] = j;
        dp[i][j] = dp[i - 1][j - 1], if word1[i - 1] = word2[j - 1];
        dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1), otherwise.

        :param word1: 
        :param word2: 
        :return: 
        """
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(l2)] for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))
        return dp[-1][-1]

    def minDistance2(self, word1, word2):
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [j for j in range(l2)]
        for i in range(1, l1):
            cur = [i] * l2
            for j in range(1, l2):
                cur[j] = min(cur[j - 1] + 1, pre[j] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]
        return pre[-1]


if __name__ == '__main__':
    print Solution().minDistance('hello', 'halloo')
    print Solution().minDistance2('hello', 'halloo')
