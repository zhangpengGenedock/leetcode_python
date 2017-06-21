class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        res = []
        for s in path:
            if s == '' or s == '.':
                continue
            elif s == '..':
                if len(res) != 0: res.pop()
            else:
                res.append(s)
        return '/' + '/'.join(res)

    def simplifyPath2(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [p for p in path.split('/') if p != '' and p != '.']
        stack = []
        for p in path:
            if p == '..':
                if stack: stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    assert Solution().simplifyPath("/a/./b/../../c/") == "/c"
    assert Solution().simplifyPath("/home/") == "/home"
    assert Solution().simplifyPath2("/a/./b/../../c/") == "/c"
    assert Solution().simplifyPath2("/home/") == "/home"
