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
