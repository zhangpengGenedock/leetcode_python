"""A sequence of number is called arithmetic if it consists of at least three elements and if the difference between
any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P,
Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

"""


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        offical solution: https://leetcode.com/problems/arithmetic-slices/solution/
        :type A: List[int]
        :rtype: int
        """
        dp, sum = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp = 1 + dp
                sum += dp
            else:
                dp = 0
        return sum

    def numberOfArithmeticSlices(self, A):
        count, sum = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                count += 1
            else:
                sum += (count + 1) * count / 2
                count = 0
        sum += count * (count + 1) / 2
        return sum
