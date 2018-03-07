"""
https://leetcode.com/problems/string-to-integer-atoi/description/

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

 

Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        ans = 0
        sin_flag = 1
        str = str.lstrip()

        if str and str[0] in ['-', '+']:
            if str[0] == '-':
                sin_flag = -1
            str = str[1:]

        for c in str:
            if not c.isdigit():
                if ans == 0:
                    return ans
                break
            ans *= 10
            ans += int(c)

        ans = ans * sin_flag
        if ans > INT_MAX:
            return INT_MAX
        elif ans < INT_MIN:
            return INT_MIN
        else:
            return ans

    def myAtoi2(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT:
                return MAX_INT
            elif result < MIN_INT:
                return MIN_INT
            else:
                return result
        except:
            return 0


if __name__ == '__main__':
    assert Solution().myAtoi('  -532de43') == -532
    assert Solution().myAtoi2('  -532de43') == -532
