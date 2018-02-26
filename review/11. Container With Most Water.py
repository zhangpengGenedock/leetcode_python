"""
https://leetcode.com/problems/container-with-most-water/description/

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


"""
class Solution(object):
    def maxArea(self, height):
        """
        https://discuss.leetcode.com/topic/16754/simple-and-fast-c-c-with-explanation
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        water = 0
        while i < j:
            h = min(height[i], height[j])
            water = max(water, h * (j - i))
            while height[i] <= h and i < j: i += 1
            while height[j] <= h and j > i: j -= 1
        return water
