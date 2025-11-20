# Leetcode 3378: Count Connected Components in LCM Graph
# https://leetcode.com/problems/count-connected-components-in-lcm-graph/
# Solved on 20th of November, 2025
class Solution:
    def countComponents(self, nums: list[int], threshold: int) -> int:
        """
        Counts the number of connected components in an LCM graph.

        :param nums: A list of integers representing the nodes in the graph.
        :param threshold: An integer representing the maximum value for consideration in the graph.
        :return: The number of connected components.
        """
        parent = list(range(threshold + 1))

        def find(i):
            root = i
            while root != parent[root]:
                root = parent[root]
            curr = i
            while curr != root:
                nxt = parent[curr]
                parent[curr] = root
                curr = nxt
            return root

        def union(i, j):
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                parent[rootI] = rootJ
                return True
            return False

        exists = [False] * (threshold + 1)
        for num in nums:
            if num <= threshold:
                exists[num] = True

        componentCount = len(nums)

        for g in range(1, threshold // 2 + 1):
            limit = threshold // g
            limitI = int(limit ** 0.5)

            for i in range(1, limitI + 1):
                x = i * g
                if not exists[x]:
                    continue

                limitJ = limit // i
                for j in range(i + 1, limitJ + 1):
                    y = j * g
                    if exists[y]:
                        if union(x, y):
                            componentCount -= 1

        return componentCount