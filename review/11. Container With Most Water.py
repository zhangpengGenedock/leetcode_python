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
