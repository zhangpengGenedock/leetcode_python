"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

{@link https://leetcode.com/static/images/problemset/histogram.png}


The largest rectangle is shown in the shaded area, which has area = 10 unit.

https://leetcode.com/static/images/problemset/histogram_area.png

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""
class Solution(object):
    def largestRectangleArea(self, height):
        """
        https://discuss.leetcode.com/topic/27840/ac-python-clean-solution-using-stack-76ms
        
        The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the 
        building who is taller than the new one. The building popped out represent the height of a rectangle with the 
        new building as the right boundary and the current stack top as the left boundary. Calculate its area and 
        update ans of maximum area. Boundary is handled using dummy buildings. 
        
        
        :param height: 
        """
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans


if __name__ == '__main__':
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
