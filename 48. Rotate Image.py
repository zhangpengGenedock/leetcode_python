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


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print matrix
    Solution().rotate2(matrix)
    print matrix
