# Leetcode 1049: Last Stone Weight II
# https://leetcode.com/problems/last-stone-weight-ii/
# Solved on 4th of August, 2025
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        Given an array of integers `stones` representing the weights of stones,
        return the smallest possible non-negative weight of the last stone.

        Args:
            stones (list[int]): A list of integers representing the weights of the stones.
        Returns:
            int: The smallest possible non-negative weight of the last stone.
        """
        totalSum = sum(stones)
        target = totalSum // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for j in range(target, stone -1, -1):
                dp[j] = dp[j] or dp[j - stone]

        maxSum = 0
        for i in range(target, -1, -1):
            if dp[i]:
                maxSum = i
                break

        return totalSum - 2 * maxSum