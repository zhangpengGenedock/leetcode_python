class Solution(object):
    def judgeCircle(self, moves):
        """
        question: https://leetcode.com/problems/judge-route-circle/description/
        solution: https://leetcode.com/problems/judge-route-circle/solution/
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for move in moves:
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
        return x == y == 0

    def judgeCircle2(self, moves):
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
