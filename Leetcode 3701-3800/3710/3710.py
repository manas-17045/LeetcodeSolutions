# Leetcode 3710: Maximum Partition Factor
# https://leetcode.com/problems/maximum-partition-factor/
# Solved on 21st of December, 2025
class Solution:
    def maxPartitionFactor(self, points: list[list[int]]) -> int:
        """
        Calculates the maximum partition factor for a given set of points.
        :param points: A list of lists, where each inner list represents a point [x, y].
        :return: The maximum partition factor.
        """
        n = len(points)
        if n == 2:
            return 0

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))

        edges.sort(key=lambda x: x[0])

        parent = list(range(n))
        diff = [0] * n

        def find(i):
            if parent[i] != i:
                root, rootDiff = find(parent[i])
                parent[i] = root
                diff[i] = (diff[i] + rootDiff) % 2
            return parent[i], diff[i]

        def union(i, j):
            rootI, diffI = find(i)
            rootJ, diffJ = find(j)

            if rootI != rootJ:
                parent[rootI] = rootJ
                diff[rootI] = (1 - diffI + diffJ) % 2
                return True
            else:
                return diffI != diffJ

        for dist, u, v in edges:
            if not union(u, v):
                return dist

        return 0