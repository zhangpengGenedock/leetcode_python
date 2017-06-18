class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            k = ''.join(sorted(s))
            if k in m:
                m[k].append(s)
            else:
                m[k] = [s]
        # return [m[k] for k in m]
        return m.values()

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for item in strs:
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic.get(sortedItem, []) + [item]
        return dic.values()


    def groupAnagrams3(self, strs):
        import collections
        dic = collections.defaultdict(list)
        for item in strs:
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic[sortedItem] + [item]
        return dic.values()


if __name__ == '__main__':
    print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print Solution().groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])
    print Solution().groupAnagrams3(["eat", "tea", "tan", "ate", "nat", "bat"])
