"""
https://leetcode.com/problems/candy/description/

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
class Solution(object):
    def candy(self, ratings):
        """
        https://discuss.leetcode.com/topic/21025/simple-python-solution-with-two-passes
        :type ratings: List[int]
        :rtype: int
        """
        res = [1] * len(ratings)
        lbase = rbase = 1
        for i in xrange(1, len(ratings)):
            lbase = lbase + 1 if ratings[i] > ratings[i - 1] else 1
            res[i] = lbase

        for i in xrange(len(ratings) - 2, -1, -1):
            rbase = rbase + 1 if ratings[i] > ratings[i + 1] else 1
            res[i] = max(rbase, res[i])
        return sum(res)
