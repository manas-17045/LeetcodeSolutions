# Leetcode 1872: Stone Game VIII
# https://leetcode.com/problems/stone-game-viii/
# Solved on 26th of July, 2025
class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        """
        Calculates the maximum score difference Alice can achieve in the Stone Game VIII.

        Args:
            stones: A list of integers representing the values of the stones.
        Returns:
            The maximum score difference Alice can achieve.
        """

        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # maxDiff represents the value of dp[i] as we iterate backwards.
        maxDiff = prefix[n]

        # Iterate backwards from i = n - 2 down to 1 to compute dp[1].
        for i in range(n - 2, 0, -1):
            maxDiff = max(maxDiff, prefix[i + 1] - maxDiff)

        return maxDiff