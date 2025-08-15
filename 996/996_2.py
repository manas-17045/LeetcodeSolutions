# Leetcode 996: Number of Squareful Arrays
# https://leetcode.com/problems/number-of-squareful-arrays/
# Solved on 15th of August, 2025
import math
from collections import Counter
from functools import lru_cache


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        """
        Calculates the number of squareful permutations of a given list of integers.
        A permutation is squareful if the sum of every two adjacent elements is a perfect square.

        Args:
            nums: A list of integers.
        Returns:
            The number of squareful permutations.
        """
        if not nums:
            return 0

        # Unique values and their counts
        counter = Counter(nums)
        vals = list(counter.keys())
        counts = [counter[v] for v in vals]
        m = len(vals)

        # Precompute adjacency: can i be next to j?
        neighbors = [[] for _ in range(m)]
        for i in range(m):
            for j in range(m):
                s = vals[i] + vals[j]
                # Check perfect square using math.isqrt for correctness
                root = math.isqrt(s)
                if root * root == s:
                    neighbors[i].append(j)

        # DFS with memoization
        @lru_cache(None)
        def dfs(prev: int, counts_state: tuple) -> int:
            # counts_state is a tuple of remaining counts for each unique value
            if sum(counts_state) == 0:
                return 1

            total = 0
            if prev == -1:
                # Choose any starting value
                for i in range(m):
                    new_counts = list(counts_state)
                    new_counts[i] -= 1
                    total += dfs(i, tuple(new_counts))
            else:
                # Choose only neighbors that still have remaining count
                for j in neighbors[prev]:
                    if counts_state[j] > 0:
                        new_counts = list(counts_state)
                        new_counts[j] -= 1
                        total += dfs(j, tuple(new_counts))

            return total

        return dfs(-1, tuple(counts))