# Leetcode 952: Largest Component Size by Common Factor
# https://leetcode.com/problems/largest-component-size-by-common-factor/
# Solved on 13th of July, 2025
import collections


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        """
        Finds the size of the largest connected component in a graph where nodes are numbers
        from `nums`, and an edge exists between two numbers if they share a common factor greater than 1.

        This problem can be modeled as finding the largest connected component in a graph.
        Instead of directly connecting numbers, we connect numbers to their prime factors.
        If two numbers share a common prime factor, they will be indirectly connected through that factor.

        The algorithm uses a Disjoint Set Union (DSU) data structure to manage the connected components.
        It also precomputes the smallest prime factor (SPF) for numbers up to the maximum in `nums`
        using a sieve-like approach.

        Args:
            nums: A list of integers.

        Returns:
            The size of the largest connected component.

        Complexity:
            Time: O(N log M + M log log M), where N is the number of elements in `nums` and M is the maximum value in `nums`.
            Space: O(M) for DSU arrays and SPF array.
        """
        if not nums:
            return 0

        limit = max(nums)
        parent = list(range(limit + 1))
        componentSize = [1] * (limit + 1)

        def find(i: int) -> int:
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> None:
            rootI = find(i)
            rootJ = find(j)
            if rootI != rootJ:
                if componentSize[rootI] < componentSize[rootJ]:
                    rootI, rootJ = rootJ, rootI
                parent[rootJ] = rootI
                componentSize[rootI] += componentSize[rootJ]

        spf = list(range(limit + 1))
        i = 2
        while i * i <= limit:
            if spf[i] == i:
                for j in range(i * i, (limit + 1), i):
                    if spf[j] == j:
                        spf[j] = i
            i += 1

        for num in nums:
            n = num
            while n > 1:
                primeFactor = spf[n]
                union(num, primeFactor)
                while n % primeFactor == 0:
                    n //= primeFactor

        maxSize = 0
        groupSizes = collections.defaultdict(int)
        for num in nums:
            root = find(num)
            groupSizes[root] += 1
            maxSize = max(maxSize, groupSizes[root])

        return maxSize