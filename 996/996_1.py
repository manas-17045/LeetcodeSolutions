# Leetcode 996: Number of Squareful Arrays
# https://leetcode.com/problems/number-of-squareful-arrays/
# Solved on 15th of August, 2025
import collections


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        """
        Calculates the number of squareful permutations of the given array `nums`.

        Args:
            nums (list[int]): The input array of integers.
        Returns:
            int: The number of squareful permutations.
        """
        counts = collections.Counter(nums)
        graph = {x: [] for x in counts}

        def isSquare(n):
            root = int(n**0.5)
            return root * root == n

        for x in counts:
            for y in counts:
                if isSquare(x + y):
                    graph[x].append(y)

        n = len(nums)

        def dfs(node, remaining):
            if remaining:
                return 1

            counts[node] -= 1

            res = 0
            for neighbor in graph[node]:
                if counts[neighbor] > 0:
                    res += dfs(neighbor, remaining - 1)

            counts[node] += 1
            return res

        total = 0
        for num in counts.keys():
            total += dfs(num, n)

        return total