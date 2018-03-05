"""
https://leetcode.com/problems/word-search/description/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist_from_index(self, board, word, i, j, s, used):
        if s == len(word) - 1:
            return True
        m, n = len(board), len(board[0])
        used[i][j] = True
        result = (
                     i + 1 < m and word[s + 1] == board[i + 1][j] and used[i + 1][j] == False and self.exist_from_index(
                         board,
                         word,
                         i + 1,
                         j,
                         s + 1,
                         used)) or (
                     i - 1 >= 0 and word[s + 1] == board[i - 1][j] and used[i - 1][
                         j] == False and self.exist_from_index(
                         board, word, i - 1, j, s + 1, used)) or (
                     j - 1 >= 0 and word[s + 1] == board[i][j - 1] and used[i][
                         j - 1] == False and self.exist_from_index(
                         board, word, i, j - 1, s + 1, used)) or (
                     j + 1 < n and word[s + 1] == board[i][j + 1] and used[i][j + 1] == False and self.exist_from_index(
                         board,
                         word,
                         i,
                         j + 1,
                         s + 1,
                         used))
        used[i][j] = False
        return result

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    used = [[False] * len(board[0]) for _ in range(len(board))]
                    used[i][j] = True
                    if self.exist_from_index(board, word, i, j, 0, used):
                        return True
        return False

    def exist2(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) or self.dfs(board, i, j - 1,
                                                                                                     word[
                                                                                                     1:]) or self.dfs(
            board, i, j + 1, word[1:])
        board[i][j] = tmp
        return res


if __name__ == '__main__':
    assert Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'ABCCED') == True

    assert Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'SEE') == True

    assert Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'ABCB') == False

    assert Solution().exist(["CAA", "AAA", "BCD"]
                            , "AAB") == True

    assert Solution().exist(["ABCE", "SFES", "ADEE"]
                            , "ABCESEEEFS") == True

    assert Solution().exist2([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'ABCCED') == True

    assert Solution().exist2([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'SEE') == True

    assert Solution().exist2([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], 'ABCB') == False

    assert Solution().exist2(["CAA", "AAA", "BCD"]
                            , "AAB") == True

    assert Solution().exist2(["ABCE", "SFES", "ADEE"]
                            , "ABCESEEEFS") == True
