# Leetcode 1799: Maximize Score After N Operations
# https://leetcode.com/problems/maximize-score-after-n-operations/
# Solved on 11th of June, 2025
import math
from functools import lru_cache


class Solution:
    def maxScore(self, nums: list[int]) -> int:
        """
        Calculates the maximum score achievable by performing operations on pairs of numbers.

        The operations are performed in order from 1 to n (where 2n is the length of nums).
        In the i-th operation, we choose two unused numbers from nums, say x and y,
        and receive a score of i * gcd(x, y). The goal is to maximize the total score.

        Args:
            nums: A list of integers of even length.

        Returns:
            The maximum possible score.
        """

        m = len(nums)
        full_mask = (1 << m) - 1

        # Precompute pairwise gcds
        gcd_mat = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range((i + 1), m):
                gcd_mat[i][j] = math.gcd(nums[i], nums[j])

        @lru_cache(None)
        def dfs(mask: int) -> int:
            # If mask == full_mask, then all numbers are used
            if mask == full_mask:
                return 0

            used = mask.bit_count()
            # Operation index is (used/2) + 1, since each operation used 2 numbers
            op = used // 2 + 1

            best = 0
            # Pick two unused numbers i < j
            for i in range(m):
                if (mask >> i) & 1:
                    continue
                for j in range((i + 1), m):
                    if (mask >> j) & 1:
                        continue
                    new_mask = mask | (1 << i) | (1 << j)
                    score = op * gcd_mat[i][j] + dfs(new_mask)
                    if score > best:
                        best = score

            return best

        # Start with no number used
        return dfs(0)