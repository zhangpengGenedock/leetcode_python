class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        import itertools
        return list(itertools.combinations(range(1, n + 1), k))

    def combine2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(1, n + 1) for pre in self.combine2(i - 1, k - 1)]

    def combine3(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        return combs

    def combine4(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return reduce(lambda C, _: [[i] + c for c in C for i in range(1, c[0] if c else n + 1)],
                      range(k), [[]])


if __name__ == '__main__':
    print Solution().combine(5, 3)
    print Solution().combine2(5, 3)
    print Solution().combine3(5, 3)
    print Solution().combine4(5, 3)
