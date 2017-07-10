class Solution(object):
    def getRow(self, rowIndex):
        """
        https://discuss.leetcode.com/topic/15559/very-simple-python-solution/2
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
