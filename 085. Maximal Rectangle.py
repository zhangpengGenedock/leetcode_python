"""
https://leetcode.com/problems/maximal-rectangle/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
"""
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        The solution is based on largest rectangle in histogram solution. Every row in the matrix is viewed as the 
        ground with some buildings on it. The building height is the count of consecutive 1s from that row to above 
        rows. The rest is then the same as this solution for largest rectangle in histogram 
        
        :param matrix: 
        :return: 
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in xrange(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in xrange(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


if __name__ == '__main__':
    print Solution().maximalRectangle(
        [['1', '0', '1', '0', '0'],
         ['1', '0', '1', '1', '1'],
         ['1', '1', '1', '1', '1'],
         ['1', '0', '0', '1', '1']])
