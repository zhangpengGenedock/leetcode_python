"""
https://leetcode.com/problems/simplify-path/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
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
