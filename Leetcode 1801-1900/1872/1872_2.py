# Leetcode 1872: Stone Game VIII
# https://leetcode.com/problems/stone-game-viii/
# Solved on 26th of July, 2025
class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:

        """
        Calculates the maximum score a player can achieve in Stone Game VIII.
        :param stones: A list of integers representing the values of stones.
        :return: The maximum score the first player can achieve.
        """

        n = len(stones)
        # Compute prefix sums: pre[i] = sum of stones[0] through stones[i]
        pre = [0] * n
        pre[0] = stones[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + stones[i]

        # dp_next will hold dp[i+1], initialized to dp[n-1] = pre[n-1]
        dp_next = pre[-1]

        # Iterate from i = n-2 down to 1
        # dp[i] = max(dp[i+1], pre[i] - dp[i+1])
        for i in range(n - 2, 0, -1):
            take = pre[i] - dp_next
            skip = dp_next
            dp_next = max(skip, take)

        # The answer of the full game is dp[1]
        return dp_next