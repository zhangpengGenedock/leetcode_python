"""
https://leetcode.com/problems/restore-ip-addresses/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        https://discuss.leetcode.com/topic/67096/dfs-in-python
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, s, 4, [])
        return ['.'.join(x) for x in ans]

    def helper(self, ans, s, k, temp):
        if len(s) > 3 * k:
            return
        if k == 0:
            ans.append(temp[:])
        else:
            for i in range(min(3, len(s) - k + 1)):
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    continue
                self.helper(ans, s[i + 1:], k - 1, temp + [s[:i + 1]])


if __name__ == '__main__':
    # print Solution().restoreIpAddresses('05525511135')
    print Solution().restoreIpAddresses('17204548')
