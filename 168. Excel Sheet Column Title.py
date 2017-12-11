# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.


class Solution:
    def convertToTitle(self, n):
        """
        迭代形式
        :type n: int
        :rtype: str
        """
        result = []
        while n > 0:
            result.append(chr((n - 1) % 26 + ord('A')))
            n = (n - 1) // 26
        result.reverse()
        return ''.join(result)

    def convertToTitle2(self, n):
        """
        递归形式
        :param n: 
        :return: 
        """
        return "" if n == 0 else self.convertToTitle2((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))
