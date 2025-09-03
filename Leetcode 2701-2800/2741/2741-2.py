# Leetcode 2741: Special Permutations
# https://leetcode.com/problems/special-permutations/
# Solved on 3rd of September, 2025
class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        """
        Calculates the number of special permutations of the given array `nums`.
        A permutation is special if for every two adjacent elements `x` and `y`,
        either `x` is divisible by `y` or `y` is divisible by `x`.

        Args:
            nums: A list of integers.
        Returns:
            The number of special permutations modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums)
        # Precompute which index can follow which index
        nexts = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    nexts[i].append(j)

        full = (1 << n) - 1
        dp = [[0] * n for _ in range(1 << n)]

        # base: single-element permutations
        for i in range(n):
            dp[1 << i][i] = 1

        # Iterate over all masks
        for mask in range(1 << n):
            # Try to extend permutations ending ar each possible last index
            for last in range(n):
                if not (mask & (1 << last)):
                    continue
                cur = dp[mask][last]
                if cur == 0:
                    continue
                # Try to append a valid next index
                for j in nexts[last]:
                    if mask & (1 << j):
                        continue
                    dp[mask | (1 << j)][j] = (dp[mask | (1 << j)][j] + cur) % MOD

        # Sum all permutations that used all items
        ans = sum(dp[full][i] for i in range(n)) % MOD
        return ans