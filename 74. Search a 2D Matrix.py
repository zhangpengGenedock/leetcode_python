"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        https://discuss.leetcode.com/topic/10211/a-python-binary-search-solution-o-logn
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / n][mid % n]

            if num == target:
                return True
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == '__main__':
    # assert Solution().searchMatrix([
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ]
    #     , 3) == True
    # assert Solution().searchMatrix([[1]], 1) == True
    assert Solution().searchMatrix([[1,1]],2) == False
