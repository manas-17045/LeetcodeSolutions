# Leetcode 3493: Properties Graph
# https://leetcode.com/problems/properties-graph/
# Solved on 25th of September, 2025
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        # Union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

class Solution:
    def numberOfComponents(self, properties: list[list[int]], k: int) -> int:
        """
        Calculates the number of connected components based on the similarity of properties.

        Args:
            properties: A list of lists of integers, where each inner list represents the properties of an item.
            k: An integer representing the minimum number of common properties required for two items to be considered connected.
        Returns:
            The number of connected components.
        """
        n = len(properties)
        if n == 0:
            return 0

        # Precompute sets of distinct integers for each properties[i]
        sets = [set(arr) for arr in properties]

        uf = UnionFind(n)

        # For each unique pair, check if intersection size >= k.
        for i in range(n):
            si = sets[i]
            # Skip trivial case where set size < k (can't possibly have k common)
            if len(si) < k:
                continue
            for j in range(i + 1, n):
                sj = sets[j]
                if len(sj) < k:
                    continue

                # Iterate the smaller set and count common elements, early exit when count reaches k.
                if len(si) <= len(sj):
                    smaller, larger = si, sj
                else:
                    smaller, larger = sj, si

                cnt = 0
                # Small optimization: if the smaller set size < k, cannot reach k.
                if len(smaller) < k:
                    continue

                for val in smaller:
                    if val in larger:
                        cnt += 1
                        if cnt >= k:
                            uf.union(i, j)
                            break

        # Count distinct roots (connected components)
        roots = set()
        for i in range(n):
            roots.add(uf.find(i))

        return len(roots)