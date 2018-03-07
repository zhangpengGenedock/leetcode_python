"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))

    def rotate2(self, matrix):
        n = len(matrix)
        for i in range(n / 2):
            for j in range(n - n / 2):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], \
                                                                             matrix[j][~i], matrix[i][j]

    def rotate3(self, matrix):
        """
        思路：一维的时候翻转然后翻转，二维的时候翻转,然后转置
        
        /*
         * clockwise rotate
         * first reverse up to down, then swap the symmetry 
         * 1 2 3     7 8 9     7 4 1
         * 4 5 6  => 4 5 6  => 8 5 2
         * 7 8 9     1 2 3     9 6 3
        */
        
        :param matrix: 
        :return: 
        """
        matrix.reverse()
        n = len(matrix[0])
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print matrix
    Solution().rotate2(matrix)
    print matrix
