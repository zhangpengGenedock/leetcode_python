class Solution(object):
    def generateParenthesis(self, n):
        """
        https://discuss.leetcode.com/topic/17510/4-7-lines-python
        :type n: int
        :rtype: List[str]
        """

        def generate(p, left, right, parens):
            if left:         generate(p + '(', left - 1, right, parens)
            if right > left: generate(p + ')', left, right - 1, parens)
            if not right:    parens += [p]

        parens = []
        generate('', n, n, parens)
        return parens


if __name__ == '__main__':
    print Solution().generateParenthesis(5)
