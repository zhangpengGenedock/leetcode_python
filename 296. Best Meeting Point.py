"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.
"""


class Solution(object):
    def minTotalDistance(self, grid):
        """
        offical solution: https://leetcode.com/problems/best-meeting-point/solution/
        personal solution: https://leetcode.com/problems/best-meeting-point/discuss/74193/
        :type grid: List[List[int]]
        :rtype: int
        """
        row_sum = map(sum, grid)
        col_sum = map(sum, zip(*grid))

        def min_total_distance_1d(vec):
            i, j = -1, len(vec)
            d = left = right = 0
            while i != j:
                if left < right:
                    d += left
                    i += 1
                    left += vec[i]
                else:
                    d += right
                    j -= 1
                    right += vec[j]
            return d

        return min_total_distance_1d(row_sum) + min_total_distance_1d(col_sum)
