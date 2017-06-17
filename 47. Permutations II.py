class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        result = set()
        for permut in itertools.permutations(nums, len(nums)):
                result.add(permut)

        return [list(v) for v in result]


if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 2])
