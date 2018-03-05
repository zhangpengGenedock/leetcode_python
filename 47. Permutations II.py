"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
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

    def permuteUnique2(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in xrange(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    # if i < len(l) and l[i] == n:
                    if i < len(l) and l[i] == n: #index check is for forbidden out of index exception
                        break  # handles duplication
            ans = new_ans
        return ans


if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 2])
    print Solution().permuteUnique2([1, 1, 2])
