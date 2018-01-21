class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        l = [0] * 26
        for c in tasks:
            l[ord(c) - ord('A')] += 1
        l.sort()
        time = 0
        while l[25] > 0:
            i = 0
            while i <= n:
                if l[25] == 0:
                    break
                if i < 26 and l[25 - i] > 0:
                    l[25 - i] -= 1
                time += 1
                i += 1
            l.sort()
        return time

    def leasetInterval2(self, tasks, n):
        """
        from submission
        :param tasks:
        :param n:
        :return:
        """
        task_count = [0] * 26
        for task in tasks:
            task_count[ord(task) - ord('A')] += 1

        task_count.sort(reverse=True)
        idx = 0
        while idx < 25 and task_count[idx] == task_count[0]:
            idx += 1

        return max(len(tasks), (task_count[0] - 1) * (n + 1) + idx)

    def leasetInterval3(self, tasks, n):
        """
        from submission
        :param tasks:
        :param n:
        :return:
        """
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] += 1
        # count = sorted(count)
        # maxRow = count[-1] - 1
        maxRow = max(count) - 1
        idle = (n + 1) * maxRow
        for i in range(25, -1, -1):
            idle -= min(maxRow, count[i])
        result = len(tasks) if idle < 0 else len(tasks) + idle
        return result
