"""
https://leetcode.com/problems/increasing-triplet-subsequence/description/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        https://discuss.leetcode.com/topic/39807/python-easy-o-n-solution/2
        
        C1 = so far best candidate of end element of a one-cell subsequence to form a triplet subsequence

        C2 = so far best candidate of end element of a two-cell subsequence to form a triplet subsequence
        
        Your solution is just to keep a window of size=3, and keep updating the c1 and c2 just like the LIS(longest 
        increasing sequence) Problem. but we know the size=3, so we need do not need to use the binary search to find 
        the updating position, so we can do it in O(N). 
        
        :type nums: List[int] 
        :rtype: bool 
        """
        first = second = float('Inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
