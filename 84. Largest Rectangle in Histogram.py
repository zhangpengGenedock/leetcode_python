class Solution(object):
    def largestRectangleArea(self, height):
        """
        https://discuss.leetcode.com/topic/27840/ac-python-clean-solution-using-stack-76ms
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
