# question: https://leetcode.com/problems/fizz-buzz/description/

class Solution(object):
    def fizzBuzz(self, n):
        """
        solution: https://discuss.leetcode.com/topic/63876/python-golf
        :type n: int
        :rtype: List[str]
        """
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]
