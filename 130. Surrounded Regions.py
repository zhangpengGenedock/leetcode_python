class Solution(object):
    def solve(self, board):
        """
        https://discuss.leetcode.com/topic/18706/9-lines-python-148-ms
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        save = [ij for k in range(max(m, n)) for ij in (0, k), (m - 1, k), (k, 0), (k, n - 1)]
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)

        board[:] = [['XO'[c == 'S'] for c in row] for row in board]
