class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        offical solution: https://leetcode.com/problems/contains-duplicate-ii/solution/
        python solution: https://leetcode.com/problems/contains-duplicate-ii/discuss/61375/
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
