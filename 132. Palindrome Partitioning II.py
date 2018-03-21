"""
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


"""
class Solution(object):
    def minCut(self, s):
        """
        https://discuss.leetcode.com/topic/22388/56-ms-python-with-explanation/2
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        #add above check, can improve performance very much
        cut = [x for x in range(-1, len(s))]
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
        return cut[-1]


if __name__ == '__main__':
    print Solution().minCut('aab')
