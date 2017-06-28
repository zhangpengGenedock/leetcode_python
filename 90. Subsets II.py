class Solution(object):
    def subsetsWithDup(self, nums):
        """
        https://discuss.leetcode.com/topic/8541/simple-python-solution-without-extra-space
        :param nums:
        :return:
        """
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res

    def subsetsWithDup2(self, nums):
        """
        https://discuss.leetcode.com/topic/21152/simple-python-solution-dfs
        :param nums:
        :return:
        """
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)


if __name__ == '__main__':
    print Solution().subsetsWithDup([1, 2, 2])
    print Solution().subsetsWithDup2([1, 2, 2])
