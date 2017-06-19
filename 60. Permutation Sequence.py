import math


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n + 1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        return permutation


if __name__ == '__main__':
    print Solution().getPermutation(8, 100)
