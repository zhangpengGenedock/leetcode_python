class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        rows = [False] * m
        cols = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

    def setZeroes2(self, matrix):
        """
        https://discuss.leetcode.com/topic/20134/o-1-space-solution-in-python/4
        :param matrix:
        :return:
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])

        row_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                row_zero = True
                break

        col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if col_zero:
            for j in range(n):
                matrix[0][j] = 0

        if row_zero:
            for i in range(m):
                matrix[i][0] = 0

    def setZeroes3(self, matrix):
        """
        https://discuss.leetcode.com/topic/20134/o-1-space-solution-in-python/4
        :param matrix:
        :return:
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for tem in range(m):
                        if matrix[tem][j] != 0:
                            matrix[tem][j] = 'a'
                    for tem in range(n):
                        if matrix[i][tem] != 0:
                            matrix[i][tem] = 'a'

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
