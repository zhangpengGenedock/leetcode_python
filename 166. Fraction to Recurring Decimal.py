# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Credits:
# Special thanks to @Shangrila for adding this problem and creating all test cases.

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        https://discuss.leetcode.com/topic/7699/do-not-use-python-as-cpp-here-s-a-short-version-python-code/2
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, reminder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n), '.']
        stack = []
        while reminder not in stack:
            stack.append(reminder)
            n, reminder = divmod(reminder * 10, abs(denominator))
            result.append(str(n))

        idx = stack.index(reminder)
        result.insert(idx + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')
